<template>
	<div class="login-container">
		<!-- 用于设计logo -->
		<div class="header">
			<div class="content content-text">
				<div class="logo-t"> </div>
				<div class="slogan">
					<div class="logo-contair welcome"><text>欢迎登录</text></div>
					<div class="logo-contair logoname"><text>Nodule Sorting System</text></div>
				</div>
			</div>
			<!-- logo还未确定 -->
			<!-- 可以后面再画一下 -->
			<div class="avatar content content-img">
				<img src="https://img.icons8.com/ios/50/000000/user--v1.png" alt="user--v1" />
			</div>
		</div>
		<div class="form-contair">
			<!-- 登录表单 -->
			<form class="login-form">
				<div class="form-content content-username">
					<input type="text" placeholder="用户名" v-model="username">
				</div>
				<div class="form-content content-pwd">
					<input type="password" placeholder="密码" v-model="password">
				</div>
				<div class="form-content content-sbt">
					<button type="submit" @click="login()">登录</button>
					<view @click="register()" class="rg"><text>快来注册一个吧!</text></view>
				</div>

				<div class="form-content">
					<div>
						<checkbox id="privacyPolicy"></checkbox>
						<label for="privacyPolicy">我已阅读并同意</label>
					</div>
					<div>
						<a href="#">《Nodule Sorting System隐私政策》</a>
					</div>

				</div>
			</form>
		</div>


	</div>
</template>

<script>
	export default {
		data() {
			return {
				username: '',
				password: ''
			}
		},
		methods: {
			register(){
				uni.navigateTo({
					url:'/pages/register/register'
				})
			},
			login() {

				console.log("..........................");
				console.log("username: " + this.$data.username);
				console.log("password: " + this.$data.password);

				// 添加登录逻辑
				// 如果登录成功，则执行页面跳转
				//url: 'http://127.0.0.1:5000/login',
				uni.request({
					method: 'POST',
					url: 'http://localhost:8080/login',
					data: JSON.stringify({
						u_name: this.username,
						u_password: this.password
					}),
					dataType: 'JSON',
					success: (res) => {
						var data = res.data;
						console.log(res)
						console.log(res.data)
						// 判断返回的状态码
						if (data.code === 200) {
							// 登录成功，将用户信息存入本地缓存
							uni.setStorage({
								key: 'userInfo',
								data: data.userInfo,
								success() {
									// 存入成功后跳转到首页
									uni.switchTab({
										url: '/pages/index/index'
									});
								},
								fail() {
									// 存入失败时的处理逻辑
									uni.showToast({
										title: '存储用户信息失败',
										icon: 'none'
									});
								}
							});
						} else if (data.code === 401) {
							// 密码错误，提示用户密码错误
							uni.showToast({
								title: '密码错误，请重新输入',
								icon: 'none'
							});
						} else if (data.code === 404) {
							// 用户不存在，提示用户注册
							uni.showToast({
								title: '用户不存在，请注册',
								icon: 'none'
							});
						} else {
							// 其他错误情况，统一提示
							uni.showToast({
								title: '登录失败，请稍后重试',
								icon: 'none'
							});
						}
					},
					fail: () => {
						// 请求失败时的处理逻辑
						uni.showToast({
							title: '网络请求失败，请稍后重试',
							icon: 'none'
						});
					}

				})
				// this.goindex();
			},
			goindex() {
				uni.switchTab({
					url: '/pages/index/index'
				});
			}
		},
		onShow() {
			uni.getStorage({
				key:'loginInfo',
				success: (res) => {
					// 成功获取到用户信息后，将其赋值给组件的 username 属性
					this.username = res.data.u_name;
					this.password=res.data.u_password;
					console.log(this.username)
					console.log(this.password)
				},
				fail: () => {
					// 获取失败时的处理逻辑
					console.error("Failed to get login info from storage");
				},
			})
		},
	}
</script>

<style>
	page {
		display: flex;
		flex-direction: column;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.012);
	}

	.header {
		width: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		background-color: antiquewhite;
	}

	.content-text {
		/* background-color: rgba(0, 0, 0, 0.2); */
		/* border-right: 12px solid rgba(0, 0, 0, .8); */
		display: flex;
		flex-direction: row;
		margin-left: 40rpx;
		padding: 40rpx 0;
	}

	.login-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		height: 100%;

	}

	.slogan {
		height: 100rpx;
		flex: 0 auto;
		min-height: 100rpx;
		/* background-color: red; */
		margin-left: 20rpx;
		font-size: 46rpx;
		/* margin-bottom: 20rpx; */
		padding: 25rpx 0;
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		align-items: flex-start;
	}

	.logo-t {
		width: 15rpx;
		height: 150rpx;
		border-radius: 15rpx;
		background-color: #007bff;
	}

	.welcome {
		display: flex;
		flex-direction: column;
	}

	.welcome>text {
		font-size: 36rpx;
		font-weight: 540;

		letter-spacing: 2rpx;
	}

	.logoname {
		display: flex;
		flex-direction: column;
	}

	.logoname>text {
		font: 40rpx;
		font-weight: 800;
	}

	.avatar img {
		margin-top: 20rpx;
		width: 120rpx;
		height: 120rpx;
		margin-bottom: 30rpx;
		/* border: 1px solid red; */
	}

	/* ------------------------------------------------------------------------------ */
	.form-contair {
		width: 100%;
		flex: 1 1 auto;
		/* background-color: red; */
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.login-form {
		width: 80%;
		/* background-color: red; */
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.form-content {
		margin-bottom: 30rpx;
		max-width: 1000rpx;
		/* width: 100%; */
		min-height: 120rpx;
		display: flex;
		flex-direction: column;
		justify-content: center
	}

	.content-username,
	.content-pwd {
		background-color: rgba(0, 0, 0, 0.1);
		border-radius: 15rpx;
		padding: 0 40rpx;
	}

	.form-content>input {
		padding: 20rpx 0;
		font-size: 36rpx;
	}

	.content-sbt>button {
		width: 100%;
	}

	.content-sbt {
		margin-top: 50rpx;
		display: flex;
		flex-direction: column;
	}
	.content-sbt>.rg{
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: flex-end;
		
	}
	.rg>text{
		text-decoration: underline;
		text-decoration-style: solid;
		text-decoration-color: #007bff;
		cursor: pointer;
	}
	input {
		caret-color: #04b327;
	}

	button {
		padding: 10rpx 20rpx;
		background-color: #007bff;
		color: #fff;
		border: none;
		cursor: pointer;
		border-radius: 12rpx;
		margin-bottom: 20rpx;
		font-size: 40rpx;
		letter-spacing: 15rpx;
	}

	button:hover {
		background-color: #0056b3;
	}
</style>