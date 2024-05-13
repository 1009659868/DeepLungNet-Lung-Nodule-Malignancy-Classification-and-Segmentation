from flask import Flask,request,jsonify,send_file,send_from_directory
from PIL import Image
import os
from datetime import datetime

import dao
from IDNS import prediction
from Segmentation import prediction as segmentation
import tensorflow as tf

from sqlalchemy import select
import models
from dao import UserDao,HistoryDao
from config import *

import until

#app初始化,db初始化
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
models.init(app)

pre = None
seg = None
user_dao=UserDao()
history_dao=HistoryDao()
db=models.db

@app.route("/")
def index():

    return "welcome to Nodule-Sorting-System"

#查询病例信息,从history表中返回病例信息,可以是单个用户的所有病例信息,也可以是所有的病例信息
#可用于前端的历史记录页面,也可以用于数据分析页面




#注册
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        data = request.json
        u_name = data.get('u_name')
        u_password = data.get('u_password')
        u_email = data.get('u_email')
        u_nickname = data.get('u_nickname')

        if u_name and u_password and u_email:
            # 检查用户名是否已经存在
            if user_dao.check_username_exist(u_name):
                return jsonify({"error": "Username already exists", "code": 409}), 409

            # 调用 UserDao 的 register_user 方法进行用户注册
            success, message, code = user_dao.register_user(u_name, u_password, u_email, u_nickname)
            if success:
                print(f'register success:{u_name}')
                return jsonify({"message": message, "code": code}), code
            else:
                return jsonify({"error": message, "code": code}), code
        else:
            return jsonify({"error": "Missing username, password, or email", "code": 400}), 400
    else:
        return jsonify({"error": "Invalid request method", "code": 405}), 405

#登录
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        showRequest(request)
        data = request.json
        u_name = data.get('u_name')
        u_password = data.get('u_password')

        if u_name and u_password:
            # 调用 UserDao 的 login_user 方法进行用户验证
            success, message, user_info = user_dao.login_user(u_name, u_password)
            if success:
                return jsonify({"message": message, "userInfo": user_info,"code":200}),200
            else:
                return jsonify({"error": message,"code":401}), 401
        else:
            return jsonify({"error": "Missing username or password","code":400}), 400
    else:
        return jsonify({"error": "Invalid request method","code":405}), 405

#预测分类
@app.route("/getSort", methods=["GET", "POST"])
def getSort():
    print("come!!!")
    showRequest(request)
    #--------------------------------------------------------
    #一下内容用于接收上传数据
    # 获取前端上传的用户名
    u_name = request.form.get('username').strip('"')
    print('username:',u_name)
    if not u_name:
        return jsonify({'error': 'Username is required'}), 400

    # 获取上传的文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    print('fileType:', file.content_type)
    # 如果用户没有选择文件，浏览器也会发送一个空的文件字段
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    # 在这里，可以将上传的文件保存到指定的位置
    save_folder='img/'
    # 根据当前时间生成文件名，组合命名
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    print(file.filename)
    print(file.filename.split('.')[-1])
    new_file_name = f"{u_name}_{timestamp}_before.{file.filename.split('.')[-1]}"

    # 构建新文件路径
    new_file_path = os.path.join(save_folder, new_file_name)
    file.save(new_file_path)
    #将识别结果返回给前端
    if(Image.open(new_file_path)!=None):
        print("save success do somthing")
    #------------------------------------------------------
    #以下内容用处理接收到的数据,预测,并写入history
    global pre
    if pre is None:
        pre = prediction.Pre()
    global seg
    if seg is None:
        seg=segmentation.Seg()

    print("file_path:", new_file_path)
    #恶性程度预测
    response= until.predict(pre,new_file_path)
    print("response",response)

    max_prob_value, max_prob_key=until.find_max_probability(response)
    prob=f"{max_prob_key}({max_prob_value * 100:.4f}%)"
    advise=''
    if(max_prob_key=='1.高度不太可能'):
        advise='尽量保持健康的生活方式，包括定期锻炼、均衡饮食和避免有害物质。'
    elif max_prob_key=='2.中度不太可能' :
        advise ='保持定期体检，及时发现任何健康问题并寻求医疗建议。'
    elif max_prob_key=='3.不确定的':
        advise ='积极争取更多的健康信息，寻求专业医生的建议，并进行必要的检查。'
    elif max_prob_key=='4.中度可疑':
        advise ='加强健康监测，定期进行体检，并注意任何异常症状。'
    else:
        advise='立即寻求专业医疗建议，进行详细的检查和治疗计划，以确保及早发现和处理任何潜在的健康问题。'
    print(prob)
    #图像分割预测
    response=until.segmentation(seg,new_file_path)
    if(response.get('code')==200):
        response=response.get('segmentation')

    #---------------------------------------------------------
    #接下来将预测结果,用户信息等存入数据库
    res= history_dao.add_history(
        date=timestamp,
        user_info={'u_name':u_name},
        image_path_before=new_file_path,
        image_path_after=response,
        result=prob,
        advise=''
    )
    print(res)
    result = {
            "code":200,
            "data":{
                "imagePath_before": new_file_name,
                "imagePath_after":response,
                "predict": prob,
                "advise": advise,
                "date": timestamp
            }
            # 添加识别结果数据
        }
    return jsonify(result)


#访问内存图片
@app.route('/showImage/<fileName>')
def showImage(fileName):
    # return f'{fileName}'
    return send_from_directory('../Back-End_Nodule-Sorting-System/img/', f'{fileName}')



#显示请求信息
def showRequest(request):
     # 输出请求方法
    print("Request Method:", request.method)

    # 输出请求表单数据
    print("Form Data:", request.form)

    # 输出请求文件数据
    print("Files:", request.files)

    # 输出请求头信息
    print("Headers:", request.headers)

    # 输出请求参数
    print("Arguments:", request.args)

    # 输出请求原始数据（通常在 POST 请求中使用）
    print("Raw Data:", request.data)



if __name__=='__main__':
    # 创建 Flask 应用上下文
    with app.app_context():
        # 在应用启动之前创建数据库表格
        models.db.create_all()

        # 在 Flask 应用中使用 TensorFlow 图的上下文管理器
        app.run(host="localhost", port=8080)

