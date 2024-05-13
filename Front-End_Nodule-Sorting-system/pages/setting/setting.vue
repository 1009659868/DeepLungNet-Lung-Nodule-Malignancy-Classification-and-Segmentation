<template>
    <view class="content">
        <div class="mui-content-padded">
			
				<!-- 列表组件 -->
				
				<div v-for="(project, index) in projectList" :key="index" @click="goProDetail(project)" class="project-block">
				    <div class="item-content" :class="{ 'special-option': project.proName === '切换账号' || project.proName === '退出登录' }">{{ project.proName }}</div>
				    <div class="item-content">{{ project.proUnit }}</div>
				    <div class="item-content">{{ project.area }}</div>
				    <div class="item-content">{{ project.proType }}</div>
				    <div class="item-content">{{ project.stage }}</div>
				    <div class="arrow-icon item-content" v-if="project.proName!='切换账号'&& project.proName != '退出登录'">
						<image  style="width: 50rpx;" mode="widthFix" src="../../static/icon/icon_right.svg"></image>
					</div>
				</div>
			
        </div>

        <!--  totalNum: 条目总数量  pageCount:设置分页数量  curPageNum:设置当前页-->
        <!-- <cc-listPageView :totalNum="totalNum" pageCount="10" :curPageNum="curPageNum" @pageClick="pageClick">
        </cc-listPageView> -->

    </view>
</template>

<script>
    export default {
        components: {},
        data() {
            return {
                totalNum: 0,
                curPageNum: 1,
                projectList: []
            }
        },
        onLoad() {
            this.requestData();
        },
        methods: {
            goProDetail(item) {
                if (item.proName === '切换账号') {
                    // 切换跳转页面
                    uni.navigateTo({
                        url: '#' 
                    });
                } else if (item.proName === '退出登录') {
                    //退出跳转页面
                    uni.navigateTo({
                        url: '#' 
                    });
                } else {
                    // 其他项目条目的点击跳转页面
                    uni.navigateTo({
                        url: '/pages/projectDetail.vue?id=' + item.id 
                    });
                }
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

                let stringsArray = [
                    "账号管理",
                    "手机号码",
                    "账号安全",
                    "隐私",
                    "关于app",
                    "帮助",
                    "深色模式",
                    "通知设置",
                    "切换账号",
                    "退出登录"
                ];

                for (let i = 0; i < stringsArray.length; i++) {
                    this.projectList.push({
                        'proName': stringsArray[i],
                        'proUnit': '',  
                        'area': '',
                        'proType': '',
                        'stage': '',
                        'id': ''
                    });
                }
            }
        }
    }
</script>

<style scoped>
	page{
		display: flex;
		flex-direction: column;
		height: 100%;
	}
	.content{
		height: 100%;
	}
	
	.mui-content-padded{
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content:space-evenly;
		background-color: rgba(0, 0, 0, 0.065);
	}
	.mui-content-padded::before{
		content: '';
		width: 300rpx;
		height: 300rpx;
		position: absolute;
		left: 40%;
		transform: translateX(-50%);
		bottom: 100rpx;
		border-radius: 50%;
		background: linear-gradient(to top left ,rgb(18,194,233),rgb(196,133,237),rgb(247,121,125));
	}
	.mui-content-padded::after{
		content: '';
		z-index: 0;
		width: 300rpx;
		height: 300rpx;
		position: absolute;
		right: 40rpx;
		transform: translateX(-25%);
		bottom: 810rpx;
		border-radius: 20%;
		background: linear-gradient(to top left ,rgb(18,194,233),rgb(196,133,237),rgb(247,121,125));
	}
    .project-block {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 25rpx 40rpx;
		margin: 0 20rpx;
        border-bottom: 1px solid rgba(255, 255, 255, 0.4); 
		border-right: 1px solid rgba(255, 255, 255, 0.4);
		border-radius: 15rpx;
        cursor: pointer;
		background-color: rgba(255, 255, 255, 0.1);
		box-shadow: 6rpx 10rpx 10rpx 8rpx rgba(0, 0, 0, 0.2);
		backdrop-filter: blur(8rpx);
		z-index: 10;
		color: rgba(0, 0, 0, 0.9);
    }
	.project-block:hover{
		box-shadow: 6rpx 10rpx 10rpx 15rpx rgba(0, 0, 0, 0.2);
		position: relative;
		top: -8rpx;
		left: 15rpx;
		
		transition: ease-in 1s;
	}
	
    .item-content{
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		/* box-shadow: 10rpx 2rpx 10rpx 5rpx rgba(0, 0, 0, 0.8); */
	}
    .arrow-icon {
        font-size: 16px; 
        color: #888; 
    }

    /* "退出账号" and "切换账号" */
    .special-option {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
        
        font-weight: bold; 
		
		letter-spacing: 10rpx;
        color: rgba(0, 0, 0, 0.9); 
        text-align: center; 
        flex: 1; 
		}
</style>