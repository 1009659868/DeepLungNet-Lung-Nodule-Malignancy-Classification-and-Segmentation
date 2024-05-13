<template>
	<view class="body" >
		<nav class="shell " :class="{ 'close': !isShow }">
			<header>
				<div class="image-text">
					<span class="image">
						<img src="#" alt="">
					</span>
					<div class="text logo-text">
						<span class="name">{{username!=""?username:"去登陆"}}</span>
						<span class="software">{{public!=""?public:"无单位"}}</span>
					</div>
				</div>
				<i class="iconfont icon-xiangyoujiantou toggle" @click="close()"></i>
			</header>
			<div class="menu-bar">
				<div class="menu">
					<li class="search-box">
						<i class="iconfont icon-sousuo icon">
						</i>

						<input type="text" placeholder="搜索...">
					</li>
					<ul class="menu-links">
						<li class="nav-link">
							<a @click="goSb('主页')">
								<i class="iconfont icon-shouye icon"></i>
								<span class="text nac-text">主页</span>
							</a>
						</li>

						<li class="nav-link">
							<a @click="goSb('我的')">
								<i class="iconfont icon-shoucangxiao icon"></i>
								<span class="text nac-text">我的</span>
							</a>
						</li>

						<li class="nav-link">
							<a @click="goSb('历史')">
								<i class="iconfont icon-lishi icon"></i>
								<span class="text nac-text">历史记录</span>
							</a>
						</li>

						<li class="nav-link">
							<a href="#">
								<i class="iconfont icon-xiaoxi icon"></i>
								<span class="text nac-text">意见反馈</span>
							</a>
						</li>

						<li class="nav-link">
							<a href="#">
								<i class="iconfont icon-fensi icon"></i>
								<span class="text nac-text">介绍</span>
							</a>
						</li>

						<li class="nav-link">
							<a @click="goSb('设置')">
								<i class="iconfont icon-chuangzuo icon"></i>
								<span class="text nac-text">设置</span>
							</a>
						</li>
					</ul>
				</div>
				<div class="bottom-content">
					<li class="">

						<a href="#" v-show="username !== '' && username !== null">
							<i class="iconfont icon-zhuxiaoyuan icon"></i>
							<span class="text nac-text">注销</span>
						</a>
						<a @click="goSb('登录')" v-show="username==='' || username === null">
							<i class="iconfont icon-zhuxiaoyuan icon"></i>
							<span class="text nac-text">登录</span>
						</a>
					</li>
					<li class="mode">
						<div class="sun-moon">
							<i class="iconfont icon-rijian icon sun"></i>
							<i class="iconfont icon-yejian icon moon"></i>
						</div>
						<span class="mode-text text">夜间模式</span>
						<div class="toggle-switch ">
							<span class="switch"></span>
						</div>
					</li>
				</div>
			</div>
		</nav>
	</view>

</template>

<!-- 需要的数据:username,public -->
<script>
	import {
		Static
	} from "vue";
	export default {
		name: "sideBar",
		data() {

			return {
				a: {
					"main": "../pages/index/index",
					"me": "../pages/me/me",
				},
				username: "", // 初始化为一个空字符串
				public: "",
				temp:{
					'--body-color': '#E4E9F7',
					'--primary-color': '#695CFE',
					'--shell-color': '#FFF',
					'--primary-color-light': '#F6F5FF',
					'--toggle-color': '#DDD',
					'--text-color': '#707070',
				},
				isShow:false
			};

		},
		created() {

		},
		methods: {
			close(){
				this.isShow=!this.isShow
				console.log('show')
			},
			goSb(i) {
				console.log(i)
				if (i == "主页") {
					console.log(i)
					uni.switchTab({
						url: "../../pages/index/index"
					})
				} else if (i == "我的") {
					uni.switchTab({
						url: "../../pages/me/me"
					})
				} else if (i == "历史") {
					uni.switchTab({
						url: "../../pages/history/history"
					})
				} else if (i == '设置') {
					uni.navigateTo({
						url: "../../pages/setting/setting"
					})
				} else if (i == "登录") {
					uni.navigateTo({
						url: "../../pages/login/login"
					})
				}

			}
		},
		//生命周期钩子 mounted,
		//它在 Vue 组件被挂载到 DOM 后调用。
		//这个钩子可以确保页面加载完成后执行相应的操作。
		mounted() {
			console.log("FAQ")
			const body = document.querySelector('body'),
				shell = body.querySelector('nav'),
				toggle = body.querySelector(".toggle"),
				searchBtn = body.querySelector(".search-box"),
				modeSwitch = body.querySelector(".toggle-switch"),
				modeText = body.querySelector(".mode-text");
			// 点击toggle元素时触发事件
			toggle.addEventListener("click", () => {
				// 切换shell元素的close类
				shell.classList.toggle("close");
			})
			// 点击searchBtn元素时触发事件
			searchBtn.addEventListener("click", () => {
				// 移除shell元素的close类
				shell.classList.remove("close");
			})
			// 点击modeSwitch元素时触发事件
			modeSwitch.addEventListener("click", () => {
				// 切换body元素的dark类
				body.classList.toggle("dark");
				// 如果body元素包含dark类
				if (body.classList.contains("dark")) {
					modeText.innerText = "白日模式";
				} else {
					modeText.innerText = "夜间模式";
				}
			});
			// 组件创建时获取存储的用户信息
			uni.getStorage({
				key: "userInfo",
				success: (res) => {
					// 成功获取到用户信息后，将其赋值给组件的 username 属性
					this.username = res.data.u_name;
					console.log(this.username)
				},
				fail: () => {
					// 获取失败时的处理逻辑
					console.error("Failed to get user info from storage");
				},
			});

		},


	}
</script>

<style>
	/* 设置全局变量 */
	:root {
		--body-color: #E4E9F7;
		--shell-color: #FFF;
		--primary-color: #695CFE;
		--primary-color-light: #F6F5FF;
		--toggle-color: #DDD;
		--text-color: #707070;
	}

	/* 深色主题变量 */
	.dark {
		--body-color: #202224;
		--shell-color: #171717;
		--primary-color: #3a3b3c;
		--primary-color-light: #3a3b3c;
		--toggle-color: #fff;
		--text-color: #ccc;
	}

	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}

	.body {
		height: 100%;

		min-width: 10vh;
		background-color: var(--body-color);

		transition: all 0.3s ease;
		position: fixed;
		top: 0;
		left: 0;
		padding: 80rpx 0;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		z-index: 7;
	}

	.shell {
		height: 100%;
		width: 100%;
		position: absolute;
		top: 0rpx;
		left: 0rpx;

		width: 250px;
		padding: 10px 16px 10px 10px;
		background: rgba(255, 255, 255, 0.056);
		box-shadow: 4rpx 4rpx 18rpx rgba(0, 0, 0, 0.6);

		backdrop-filter: blur(4rpx);
		transition: all 0.3s ease;
		position: relative;
		z-index: 10;
		border-top-right-radius: 15rpx;
		border-bottom-right-radius: 15rpx;
	}

	.close {
		width: 10px;
		background: none;
		box-shadow: none;
		backdrop-filter: blur(0px);
	}

	.shell li {
		height: 40px;
		list-style: none;
		display: flex;
		align-items: center;
		margin-top: 10px;
	}

	.image,
	.icon {
		min-width: 40px;
		border-radius: 6px;
	}

	.icon {
		min-width: 40px;
		border-radius: 6px;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		font: 300 23px '';
	}

	.text,
	.icon {
		color: #080808;
		transition: all 0.3s ease;
	}

	.text {
		font: 500 17px;
		white-space: nowrap;
		opacity: 1;
	}

	.shell.close .text {
		opacity: 0;
	}

	header {
		position: relative;
	}

	.image-text {
		display: flex;
		align-items: center;
	}

	.logo-text {
		display: flex;
		flex-direction: column;
	}

	.name {
		margin-top: 2px;
		font: 600 18px '';
	}

	.software {
		font-size: 20px;
		margin-top: -2px;
		display: block;
	}

	.image {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.image img {
		width: 45px;
		border-radius: 6px;
	}

	.toggle {
		position: absolute;
		top: 100%;
		right: -45rpx;
		transform: translateY(-50%) rotate(180deg);
		height: 100rpx;
		width: 130rpx;

		background-color: rgba(0, 0, 0, 0.586);
		color: #FFF;
		border-top-right-radius: 30rpx;
		border-bottom-right-radius: 30rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 15px;
		cursor: pointer;
		transition: all 0.3s ease;
	}

	.toggle {
		color: #ccc;
	}

	.shell.close .toggle {
		transform: translateY(-50%) rotate(0deg);
	}

	.menu {
		margin-top: 40px;
	}

	li.search-box {
		border-radius: 6px;
		background-color: #F6F5FF;
		cursor: pointer;
		transition: all 0.3s ease;
	}

	li.search-box input {
		height: 100%;
		width: 100%;
		outline: none;
		border: none;
		background-color: #F6F5FF;
		color: #707070;
		border-radius: 6px;
		font-size: 17px;
		font-weight: 500;
		transition: all 0.3s ease;
	}

	.shell li a {
		list-style: none;
		height: 100%;
		background-color: transparent;
		display: flex;
		align-items: center;
		height: 100%;
		width: 100%;
		border-radius: 6px;
		text-decoration: none;
		transition: all 0.3s ease;
	}

	.shell li a:hover {
		background-color: #695CFE;
	}

	.shell li a:hover .icon,
	.shell li a:hover .text {
		color: #FFF;
	}

	.menu-bar {
		height: calc(100% - 55px);
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		overflow-y: scroll;
	}

	.menu-bar::-webkit-scrollbar {
		display: none;
	}

	.menu-bar .mode {
		border-radius: 6px;
		background-color: #F6F5FF;
		position: relative;
		transition: all 0.3s ease;
	}

	.menu-bar .mode .sun-moon {
		height: 50px;
		width: 60px;
	}

	.mode .sun-moon i {
		position: absolute;
	}

	.mode .sun-moon i.sun {
		opacity: 0;
	}

	.toggle-switch {
		position: absolute;
		right: 0;
		height: 100%;
		min-width: 60px;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 6px;
		cursor: pointer;
	}

	.switch {
		position: relative;
		height: 22px;
		width: 40px;
		border-radius: 25px;
		background-color: #DDD;
		transition: all 0.3s ease;
	}

	.switch::before {
		content: '';
		position: absolute;
		height: 15px;
		width: 15px;
		border-radius: 50%;
		top: 50%;
		left: 5px;
		transform: translateY(-50%);
		background-color: #FFF;
		transition: all 0.3s ease;
	}

	.dark .shell li a:hover .icon,
	.dark .shell li a:hover .text {
		color: #ccc;
	}

	.dark .mode .sun-moon i.sun {
		opacity: 1;
	}

	.dark .mode .sun-moon i.moon {
		opacity: 0;
	}

	.dark .switch::before {
		left: 20px;
	}
</style>