from models import db, User,History


class UserDao:
    # 检测用户名是否存在
    def check_username_exist(self, u_name):
        user = User.query.filter_by(u_name=u_name).first()
        return user is not None

    def check_email_exist(self, u_email):
        user = User.query.filter_by(u_email=u_email).first()
        return user is not None

    def register_user(self, u_name, u_password, u_email, u_nickname=None):
        #检测用户名是否重复
        if self.check_username_exist(u_name):
            return False, "Username already exists.", 409
        # 检测邮箱是否重复
        if self.check_email_exist(u_email):
            return False, "Email already exists.", 409

        user = User(u_name=u_name, u_password=u_password, u_email=u_email, u_nickname=u_nickname)
        db.session.add(user)
        try:
            db.session.commit()
            return True, "User registered successfully.", 201
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to register user: {str(e)}", 500

    def login_user(self, u_name, u_password):
        user = User.query.filter_by(u_name=u_name, u_password=u_password).first()
        if user:
            user_info = {
                "u_id": user.u_id,
                "u_name": user.u_name,
                "u_nickname": user.u_nickname,
                "u_email": user.u_email
            }
            return True, "Login successful.", user_info
        else:
            return False, "Invalid username or password.", None

    def get_user_by_id(self, u_id):
        user = User.query.get(u_id)
        return user

    def get_user_by_name(self, u_name):
        user = User.query.filter_by(u_name=u_name).first()
        return user

    def get_user_by_email(self, u_email):
        user = User.query.filter_by(u_email=u_email).first()
        return user

    def update_user(self, user, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)
        try:
            db.session.commit()
            return True, "User updated successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to update user: {str(e)}"

    def delete_user(self, user):
        db.session.delete(user)
        try:
            db.session.commit()
            return True, "User deleted successfully."
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to delete user: {str(e)}"


class HistoryDao:
    def add_history(self,date, user_info, image_path_before,image_path_after, result, advise):
        try:
            print(user_info)
            user_id = user_info.get('u_id')
            if not user_id:
                # 如果用户信息中没有提供用户ID，则根据用户名查询用户信息
                user_name = user_info.get('u_name')
                if not user_name:
                    return False, "User information incomplete.", 400
                user = User.query.filter_by(u_name=user_name).first()
                if not user:
                    return False, "User not found.", 404
                user_id = user.u_id

            #记录当前时间

            # 创建历史记录对象并存入数据库
            history = History(
                h_date=date,
                h_imagePath_before=image_path_before,
                h_imagePath_after=image_path_after,
                d_result=result,
                d_advise=advise,
                uid=user_id
            )
            db.session.add(history)
            db.session.commit()
            return True, "History added successfully.", 201
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to add history: {str(e)}", 500

    def get_history_by_user(self, user_info):
        try:
            user_id = user_info.get('u_id')
            if not user_id:
                user_name = user_info.get('u_name')
                if not user_name:
                    return False, "User information incomplete.", 400
                user = User.query.filter_by(u_name=user_name).first()
                if not user:
                    return False, "User not found.", 404
                user_id = user.u_id

            history_records = History.query.filter_by(uid=user_id).all()
            return True, history_records, 200
        except Exception as e:
            return False, f"Failed to get history: {str(e)}", 500

    def delete_history(self, history_id):
        history = History.query.get(history_id)
        if not history:
            return False, "History not found.", 404
        db.session.delete(history)
        try:
            db.session.commit()
            return True, "History deleted successfully.", 200
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to delete history: {str(e)}", 500