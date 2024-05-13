```
注册逻辑:
用户名{
最多12位用户名,只能由字母和数字组成=>如果用户名存在,则给出提示信息:该用户名已存在=>然后清空用户名输入框内容
}
密码{
长度:8位到16位,由大小写字母组成,可包含特殊符号,数字,区分大小写,不是明文输入=>如果不是合法输入,则给出提示信息:密码12位到16位,由大小写字母组成,包含特殊符号,数字,区分大小写=>然后清空密码输入框内容
}
邮箱{
不需要验证码直接输入=>如果邮箱已经存在=>页面提示信息:该邮箱已存在=>清空邮箱输入框内容
}
手机号码{
仅支持11位的中国大陆手机号=>当输入手机号以后判断手机号是否存在=>如果存在,则给出提示信息:该手机号已存在=>清空手机号码所在的输入框的内容
}
最后如果注册成功,则跳转到登陆页面,注册失败,则弹出提示框显示注册失败
```

```vue

<template>
	<div class="container">
		<div class="register-container">
			<div class="header">
				<div class="content content-text">
					<div class="logo-t"> logo</div>
					<div class="slogan">
						<div class="logo-contair welcome"><text>欢迎注册</text></div>
						<div class="logo-contair logoname"><text>Nodule Sorting System</text></div>
					</div>
				</div>
				<div class="avatar content content-img">
					<img src="https://img.icons8.com/ios/50/000000/user--v1.png" alt="user--v1" />
				</div>
			</div>

			<div class="form-contair">
				<form class="register-form">
					<div class="form-content content-username">
						<input type="text" placeholder="用户名" v-model="username" @input="validateUsername"
							maxlength="12">
						<p v-if="usernameError" class="error">{{ usernameError }}</p>
					</div>
					<div class="form-content content-pwd">
						<input type="password" placeholder="密码" v-model="password" @input="validatePassword"
							maxlength="16" />
						<p v-if="passwordError" class="error">{{ passwordError }}</p>
					</div>
					<div class="form-content content-email">
						<input type="email" placeholder="邮箱" v-model="email" @input="validateEmail" maxlength="25" />
						<p v-if="emailError" class="error">{{ emailError }}</p>
					</div>
					<div class="form-content content-nickname">
						<input type="text" placeholder="昵称" @input="validateNickname" maxlength="30" />
						<p v-if="nicknameError" class="error">{{ nicknameError }}</p>
					</div>
					<!-- <div class="form-content content-phone">
						<input type="tel" placeholder="手机号码" v-model.number="phone" @input="validatePhone"
							maxlength="11" />
						<p v-if="phoneError" class="error">{{ phoneError }}</p>
					</div> -->

					<div class="form-content content-sbt">
						<button type="submit" @click="register()"> 注册 </button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>
<script>
	export default {
		data() {
			return {
				username: '',
				password: '',
				email: '',
				phone: '',
				nickname: '',
				usernameError: '',
				passwordError: '',
				emailError: '',
				phoneError: '',
				nicknameError: ''
			};
		},
		methods: {
			validateUsername() {
				const usernameRegex = /^[a-zA-Z0-9]{1,12}$/; // 用户名只能为数字或字母，最大长度为12,input组件已限制
				console.log(this.username)
				if (this.username != null && this.username != '') {
					if (!usernameRegex.test(this.username)) {
						this.usernameError =
							'用户名格式不正确，请输入六位大小写字母组成的用户名';
					} else {
						this.usernameError = '';
					}
				} else {
					this.usernameError = '';
				}

			},
			validatePassword() {
				const passwordRegex = /^(?=.*[A-Z])[A-Za-z\d@$!%*?&]{8,16}$/;
				if (this.password != null && this.password != '') {
					if (!passwordRegex.test(this.password)) {
						this.passwordError = '密码格式不正确，请输入8位到16位，由大小写字母组成，可包含特殊符号、数字，区分大小写';
					} else {
						this.passwordError = '';
					}
				} else {
					this.passwordError = '';
				}

			},
			validateEmail() {
				const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

				if (this.email != null && this.email != '') {
					if (!emailRegex.test(this.email)) {
						this.emailError =
							'邮箱格式不正确，请输入有效的邮箱地址';
					} else {
						this.emailError = '';
					}
				} else {
					this.emailError = '';
				}

			},
			validateNickname() {

			},
			validatePhone() {
				const phoneRegex = /^1[3-9]\d{9}$/;
				if (this.phone != null && this.phone != '') {
					if (!phoneRegex.test(this.phone)) {
						this.phoneError =
							'手机号码格式不正确，请输入11位的中国大陆手机号码';
					} else {
						this.phoneError = '';
					}
				} else {
					this.phoneError = '';
				}
			},
			register() {
				if (this.username && !this.usernameError && this.password && !this.passwordError &&
					this.email && !this.emailError) {
					// 添加注册逻辑
					uni.request({
						method: 'POST',
						url: 'http://localhost:8080/register',
						data: JSON.stringify({
							u_name: this.username,
							u_password: this.password,
							u_email: this.email,
							u_nickname: this.nickname,
							// 这里可以根据需要添加其他注册信息
						}),
						dataType: 'JSON',
						success: (res) => {
							var data = res.data;
							console.log(res);
							console.log(res.data);
							// 判断返回的状态码
							if (data.code === 201) {
								// 注册成功，跳转到登录页面
								uni.setStorage({
									key:'loginInfo',
									data:{
										u_name: this.username,
										u_password: this.password,
									},
									success(){
										// 存入成功后跳转到登录界面
										uni.navigateBack({
											url:'/pages/login/login'
										})
									},
									fail(){
										
									}
								})
								uni.navigateTo({
									url: '/pages/login/login'
								});
							} else {
								// 注册失败，弹出提示框显示错误信息
								uni.showToast({
									title: data.error || '注册失败，请稍后重试',
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
				} else {
					console.log('请填写正确的注册信息');
				}
			}
		}
	};
</script>
<style scoped>
	page {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
		background-color: #000;
	}

	.container {
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 0;
		background-image: linear-gradient(to right, #97caff, #ffffff);
		/* border:2rpx solid red; */
	}

	.register-container {
		border: 3rpx solid #ccc;
		background-color: #fff;
		width: 385rpx;
		height: 650rpx;
		border-radius: 15rpx;
		padding: 30rpx 50rpx;
		position: relative;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
	}

	.header {}

	.content {
		font-size: 30rpx;
		font-weight: bold;
		font-family: ui-rounded;
		text-align: center;
		line-height: 50rpx;
		margin-bottom: 10rpx;

	}

	.logo-t {
		font-size: 25rpx;

	}

	.avatar img {
		width: 45rpx;

	}

	.form-content input {
		width: calc(100% -20px);
		padding: 8rpx;
		display: block;
		width: 100%;
		margin-bottom: 20rpx;
		padding: 10rpx;
		border-bottom: 1rpx solid rgb(128, 125, 125);
		font-size: 15rpx;

	}

	.content-sbt button {
		text-align: center;
		padding: 10rpx;
		width: 100%;
		margin-top: 40rpx;
		background-image:
			linear-gradient(to right, #97caff, #ffffff);
		color: #fff;

	}

	.error {
		color: red;
		font-size: 14rpx;

	}
</style>


```