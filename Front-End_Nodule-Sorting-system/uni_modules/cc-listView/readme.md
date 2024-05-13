### 我的技术微信公众号

查看更多前端组件和框架信息，请关注我的技术微信公众号【前端组件开发】

![图片](https://i.postimg.cc/RZ0sjnYP/front-End-Component.jpg)

#### 使用方法

```使用方法

 <div class="mui-content-padded">
           
 <!-- 列表组件 -->
            
<cc-listView :productList="projectList" @click="goProDetail"></cc-listView>

       
 </div>

       
 <!--  totalNum: 条目总数量  pageCount:设置分页数量  curPageNum:设置当前页-->
       
 <cc-listPageView :totalNum="totalNum" pageCount="10" :curPageNum="curPageNum" @pageClick="pageClick">
       
 </cc-listPageView>

```

#### HTML代码实现部分
```html


<template>
    <view class="content">

        <div class="mui-content-padded">

            <!-- 列表组件 -->
            <cc-listView :productList="projectList" @click="goProDetail"></cc-listView>

        </div>

        <!--  totalNum: 条目总数量  pageCount:设置分页数量  curPageNum:设置当前页-->
        <cc-listPageView :totalNum="totalNum" pageCount="10" :curPageNum="curPageNum" @pageClick="pageClick">
        </cc-listPageView>

    </view>
</template>


<script>
  
    export default {
        components: {

           

        },
        data() {
            return {

                totalNum: 0,
                curPageNum: 1,

                // 列表数组
                projectList: []
            }
        },
        onLoad () {

            this.requestData();
        },
        methods: {
            // 列表条目点击事件
            goProDetail(item) {

            },
            // 分页事件
            pageClick(tag) {

                if (tag === 0) {
                    // 上一页 (不等于第一页)
                    if (this.curPageNum > 1) {

                        this.curPageNum--;
                        this.requestData();
                    }
                } else {
                    // 下一页 (不等于最后一页)
                    if (this.totalNum > (this.curPageNum * 10)) {
                        this.curPageNum++;
                        this.requestData();
                    }

                }

            },

            requestData() {

                // 模拟请求参数设置
                let reqData = {

                    'area': '',
                    "pageSize": 10,
                    "pageNo": this.curPageNum
                }
                // 模拟请求接口
                this.totalNum = 39;
                this.projectList = [];
                for (let i = 0; i < 10; i++) {

                    this.projectList.push({
                        'proName': '项目名称' + i,
                        'proUnit': '公司名称' + i,
                        'area': '广州',
                        'proType': '省级项目',
                        'stage': '已开工',
                        'id': i + ''
                    });
                }
            }
       
		}
    }
</script>


<style>
    page {

        background-color: #f7f7f7;
    }

    .content {
        display: flex;
        flex-direction: column;

    }

    .mui-content-padded {
        margin: 0px 14px;
        /* background-color: #ffffff; */
    }
</style>




```
