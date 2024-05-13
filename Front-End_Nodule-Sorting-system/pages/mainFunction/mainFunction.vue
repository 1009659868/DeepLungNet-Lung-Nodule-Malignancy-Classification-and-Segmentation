<template>
	<view class="body">
		<sideBar></sideBar>
		<view class="background"></view>
		<view class="contair">
			<view class="borderShow upload-container">
				<htz-image-upload :sourceType="['camera','album']" mediaType="image" :max="4" :action="action"
					:uploadSuccess="ImageUpload" ref="uploader">
				</htz-image-upload>
			</view>
			<view class="predict-container">
				<view class="button" @click="">
					<span></span>
					<span></span>
					<span></span>
					<span></span>
					上次诊断
				</view>
				<view class="button" @click="predict">
					<span></span>
					<span></span>
					<span></span>
					<span></span>
					辅助诊断
				</view>
			</view>
		</view>

		<!-- 如果进行诊断,且成功返回数据后显示 -->
		<view class="mask" v-if="resData&&maskShow"></view>
		<view class="pageContainer" v-if="resData&&maskShow">
			<view class="page-close" @click="pageClose"> ×
			</view>
			<view class="page-content form" v-for="(item,index) in visibleItems" :key="index">
				<view class="form-images">
					<!-- 对比图 -->
					<view class="contrast container-image" @click="imgPreview(item.imagePath_before)">
						<image class="contrast-image image-left" :src='item.imagePath_before' ></image>
					</view>
					<view class="contrast right-icon">
						<image src="../../static/icon/icon_dRight .svg"></image>
					</view>
					<view class="contrast container-image" @click="imgPreview(item.imagePath_after)">
						<image class="contrast-image image-right" :src='item.imagePath_after' ></image>
					</view>
				</view>
				<view class="form-Info">
					<!-- 结果信息栏 -->
					<view class="info-date ">
						<!-- 右上角显示诊断记录时间 -->
						<text>{{item.date}}</text>
					</view>
					<view class="info-res info">
						<span></span>
						<span></span>
						<span></span>
						<span></span>
						<view class="info-content">
							<text>诊断结果:</text><text>{{item.predict}}</text>
						</view>
					</view>
					<view class="info-advice info">
						<span></span>
						<span></span>
						<span></span>
						<span></span>
						<view class="info-content">
							<text>AI建议:</text><text>{{item.advise}}</text>
						</view>
					</view>
					<view class="info-again info">
						<span></span>
						<span></span>
						<span></span>
						<span></span>
						<view class="info-content">
							<text>不清除,再试一次...</text>
						</view>
					</view>
				</view>
			</view>
			<view class="pageChange-content">
				<view class="nextPage" @click="nextPage()"><image src="../../static/icon/icon_down.svg"></image></view>
				<view class="prePage" @click="prevPage()"><image src="../../static/icon/icon_up.svg"></image></view>
			</view>
		</view>

	</view>
</template>

<script>
	import sideBar from '../../components/sideBar.vue'
	import htzImageUpload from '../../components/htz-image-upload/htz-image-upload.vue'
	export default {
		components: {
			sideBar,
			htzImageUpload
		},
		data() {
			// action:'http://127.0.0.1:5000/getSort',
			return {
				action: 'http://localhost:8080/getSort',
				maskShow: false,
				resData: null,
				uploadLists: [],
				currentPageIndex: 0,
				itemsPerPage: 1, // 每页显示的内容数量
			}
		},
		mounted() {
			// 在组件渲染完成后，设置监听器
			this.$watch(
				() => this.$refs.uploader.uploadLists,
				(newUploadLists, oldUploadLists) => {
					// 执行方法
					this.handleUploaderChange(newUploadLists);
				}
			);
		},
		computed: {
			visibleItems() {
				const startIndex = this.currentPageIndex * this.itemsPerPage;
				const endIndex = startIndex + this.itemsPerPage;
				return this.resData.slice(startIndex, endIndex);
			},
		},
		onLoad() {

			uni.setStorage({
				key: 'predictData',
				data: [],
				success: function() {
					console.log('数据初始化成功');
				},
				fail: function(err) {
					console.error('数据初始化失败', err);
				}
			});
		},
		methods: {
			imgPreview(img){
				console.log(img)
				console.log('preview')
				uni.previewImage({
				    urls: [img], // 注意这里需要将img转为数组形式，因为urls参数需要传入一个数组
				    current: 0,
				    loop: true,
				    showmenu: true, // 设置为true以显示全屏显示按钮
					zIndex:9999,
				  });
			},
			nextPage() {
				if (this.currentPageIndex < Math.ceil(this.resData.length / this.itemsPerPage) - 1) {
					this.currentPageIndex++;
				}
			},
			prevPage() {
				if (this.currentPageIndex > 0) {
					this.currentPageIndex--;
				}
			},
			convertToChineseDateTime(timestamp) {
				// 解析年、月、日、时、分、秒
				var year = timestamp.slice(0, 4);
				var month = timestamp.slice(4, 6);
				var day = timestamp.slice(6, 8);
				var hour = timestamp.slice(8, 10);
				var minute = timestamp.slice(10, 12);
				var second = timestamp.slice(12, 14);

				// 构建中文日期时间字符串
				var chineseDateTime = year + "年" + month + "月" + day + "日 " + hour + ":" + minute + ":" + second;

				return chineseDateTime;
			},
			pageClose() {
				this.maskShow = false
				this.currentPageIndex = 0
			},
			predict() {
				this.maskShow = false
				uni.getStorage({
					key: 'predictData',
					success: (res) => {
						if ((res.data != null || res.data != []) && res.data.length > 0) {
							this.resData = res.data
							console.log('resData:', this.resData)
							this.maskShow = true
						}

					},
					fail: () => {
						this.maskShow = false
						uni.showToast({
							title: '请先提交图片,或检测网络...',
							icon: 'none', // 使用 'none' 图标来表示错误
							duration: 3000 // 提示持续时间为 2000 毫秒（2 秒）
						});

					}
				})
			},
			handleUploaderChange(newUploadLists) {
				console.log('Uploader data changed:', newUploadLists);
				// 执行其他逻辑
				// 如果图片超过8张那么自动清空
				if(newUploadLists==[]||newUploadLists.length<=0){
					uni.setStorage({
						key:'predictData',
						data:[]
					})
				}

			},
			clear() {
				console.log("list:", this.$refs.uploader.uploadLists)
				this.$refs.uploader.clearUploadLists()
			},
			ImageUpload(res) {
				console.log('uploadFileSuccess')
				var _res = JSON.parse(res.data);
				console.log(_res.data)
				if (_res.code == 200) {

					// 从本地存储中获取已有的数据
					uni.getStorage({
						key: 'predictData',
						success: (result) => {
							var existingData = result.data || []; // 如果之前没有数据，则初始化为一个空数组
							// 将新的数据追加到已有数据数组中
							_res.data.imagePath_before = 'http://localhost:8080/showImage/' + _res
								.data.imagePath_before
							_res.data.imagePath_after = 'http://localhost:8080/showImage/' + _res.data
								.imagePath_after
							_res.data.date = this.convertToChineseDateTime(_res.data.date)
							console.log(_res.data.date)
							existingData.push(_res.data);
							// 将新的数组存储回本地存储中
							uni.setStorage({
								key: 'predictData',
								data: existingData,
								success: function() {
									console.log('数据追加成功');
								},
								fail: function(err) {
									console.error('数据追加失败', err);
								}
							});
						},
						fail: (err) => {
							console.error('获取已有数据失败', err);
							// 如果获取存储失败，则初始化存储数据
							var newData = [_res.data]; // 初始化为一个包含新数据的数组
							// 将新的数组存储到本地存储中
							uni.setStorage({
								key: 'predictData',
								data: newData,
								success: function() {
									console.log('初始化存储数据成功');
								},
								fail: function(err) {
									console.error('初始化存储数据失败', err);
								}
							});
						}
					});
					// url: 'http://127.0.0.1:5000/showImage/' + _res.data.imagePath
					return {
						success: true,
						url: _res.data.imagePath_before
					}
				} else {
					return {
						success: false,
						url: ''
					}
				}
			},

		},


	}
</script>

<style>
	page {
		display: flex;
		flex-direction: column;
		height: 100%;
	}
	.background {
		position: fixed;
		top: 0;
		left: 0;
		z-index: 0;
		width: 100%;
		height: 100%;
		background-color: aquamarine;
	}
	/* 左上角光圈*/
	.background::before {
		content: '';
		position: fixed;
		top: 25rpx;
		/* 上边距约为屏幕高度的四分之一 */
		left: 40rpx;
		/* 左边距约为屏幕宽度的四分之一 */
		transform: translate(-50%, -50%);
		border-radius: 50%;
		/* opacity: 0.5; */
		filter: blur(300rpx);
		width: 1200rpx;
		/* 光圈宽度 */
		height: 1200rpx;
		/* 光圈高度 */
		background-color: #07f773;
		/* 光圈背景色 */
		z-index: 1;
	}
	.background::after {
		content: '';
		position: fixed;
		bottom: 25rpx;
		/* 下边距约为屏幕高度的四分之一 */
		right: 25rpx;
		/* 右边距约为屏幕宽度的四分之一 */
		transform: translate(50%, 50%);
		border-radius: 50%;
		
		filter: blur(100rpx);
		width: 1200rpx;
		/* 光圈宽度 */
		height: 1200rpx;
		/* 光圈高度 */
		background-color: #07f773;
		/* 光圈背景色 */
		z-index: 1;
	}
	.contair {
		position: absolute;
		z-index: 3;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.2);
		display: flex;
		flex-direction: column;

		align-items: center;
		backdrop-filter: blur(5px);
		/* border: 1px solid red; */
	}

	.borderShow {
		/* border: 1px solid red; */
	}

	.mask {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.5);
		/* 半透明黑色背景 */
		z-index: 5;
		/* 设置z-index，使mask在最顶层 */
	}

	.pageContainer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		overflow: hidden;
		position: fixed;
		/* 设置为相对定位，以便在mask之上显示 */
		z-index:6;
		/* 设置z-index，使pageContainer在mask之上 */
		background-color: #fff;
		/* 设置pageContainer的背景颜色为白色 */
		padding: 20rpx;
		/* 设置内边距 */
		border-radius: 15rpx;
		/* 设置圆角边框 */
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
		width: 80%;
		height: 80%;
		/* 设置页面居中 */
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: rgba(255, 255, 255, 0.3);
		/* 设置背景颜色为半透明白色 */
		box-shadow: 0 0 12rpx rgba(255, 255, 255, 0.2);
		backdrop-filter: blur(20rpx);
		/* 添加毛玻璃效果，10px 模糊程度可以根据需要调整 */
		overflow: hidden;
		/* 隐藏溢出内容 */
		/* border-right: 2rpx solid rgba(255, 255, 255, 0.9); */
		/* border-bottom: 2rpx solid rgba(255, 255, 255, 0.9); */
	}

	.page-close {
		background-color: #f5222d;
		font-size: 24rpx;
		position: absolute;
		width: 35rpx;
		height: 35rpx;
		line-height: 35rpx;
		text-align: center;
		top: 0;
		right: 0;
		z-index: 101;
		color: #fff;
		border-radius: 0 15rpx 0 0;
	}

	.upload-container {
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.predict-container {
		width: 75%;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		align-items: center;
		position: absolute;
		top: 85%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	.button {
		width: 200rpx;
		height: 90rpx;
		position: relative;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		font-size: 32rpx;

		color: #03a9f4;
		text-decoration: none;
		text-transform: uppercase;
		transform: 0.5s;
		letter-spacing: 8rpx;
		overflow: hidden;
		-webkit-box-reflect: below 4rpx linear-gradient(transparent, #0005);
	}

	.button:nth-child(1) {
		filter: hue-rotate(150deg);
	}

	.button:nth-child(2) {
		filter: hue-rotate(10deg);
	}

	.button:hover {
		background: #03e9f4;
		color: #fff;
		box-shadow: 0 0 5rpx #03e9f4,
			0 0 25rpx #03e9f4,
			0 0 50rpx #03a9f4,
			0 0 200rpx #03a9f4;
	}

	.button span {
		position: absolute;
		display: block;
		overflow: hidden;
	}

	.button span:nth-child(1) {
		top: 0;
		left: 0;
		width: 100%;
		height: 4rpx;
		background: linear-gradient(90deg, transparent, #03e9f4);
		animation: animate1 1s linear infinite;
	}

	@keyframes animate1 {
		0% {
			left: -100%;
		}

		50%,
		100% {
			left: 100%;
		}
	}

	.button span:nth-child(2) {
		top: -100%;
		right: 0;
		width: 4rpx;
		height: 100%;
		background: linear-gradient(180deg, transparent, #03e9f4);
		animation: animate2 1s linear infinite;
		animation-delay: 0.25s;
	}

	@keyframes animate2 {
		0% {
			top: -100%;
		}

		50%,
		100% {
			top: 100%;
		}
	}

	.button span:nth-child(3) {
		bottom: 0;
		right: -100%;
		width: 100%;
		height: 4rpx;
		background: linear-gradient(270deg, transparent, #03e9f4);
		animation: animate3 1s linear infinite;
		animation-delay: 0.5s;
	}

	@keyframes animate3 {
		0% {
			right: -100%;
		}

		50%,
		100% {
			right: 100%;
		}
	}

	.button span:nth-child(4) {
		bottom: -100%;
		left: 0;
		width: 4rpx;
		height: 100%;
		background: linear-gradient(360deg, transparent, #03e9f4);
		animation: animate4 1s linear infinite;
		animation-delay: 0.75s;
	}

	@keyframes animate4 {
		0% {
			bottom: -100%;
		}

		50%,
		100% {
			bottom: 100%;
		}
	}

	.page-content {
		width: 90%;
		height: 90%;
		/* border: 1rpx solid red; */
		border-radius: 30rpx;
	}

	.pageChange-content {
		width: 320rpx;
		height: 100rpx;
		/* border:2rpx solid red; */
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		align-items: center;
	}

	.nextPage {
		width: 80rpx;
		height: 80rpx;
		border-radius: 40rpx;
		/* border: 1rpx solid red; */
		background: #03a9f4;
		opacity: 0.8;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		box-shadow: 0 0 5rpx #03e9f4,
			0 0 25rpx #03e9f4,
			0 0 50rpx #03a9f4,
			0 0 200rpx #03a9f4;
		/* position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%); */
		z-index: 100;
		cursor: pointer;
		animation: flash 10s linear infinite;
	}
	.nextPage image{
		width: 90%;
		height: 90%;
	}
	.prePage {
		width: 80rpx;
		height: 80rpx;
		border-radius: 40rpx;
		box-shadow: 0 0 5rpx #03e9f4,
			0 0 25rpx #03e9f4,
			0 0 50rpx #03a9f4,
			0 0 200rpx #03a9f4;
		/* border: 1rpx solid red; */
		background: #03a9f4;
		opacity: 0.8;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		/* position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%); */
		z-index: 100;
		cursor: pointer;

		animation: flash 10s linear infinite;
	}
	.prePage image{
		width: 90%;
		height: 90%;
	}
	@keyframes flash {
		0% {
			box-shadow: 0 0 5rpx #03e9f4,
				0 0 25rpx #03e9f4,
				0 0 50rpx #03a9f4,
				0 0 200rpx #03a9f4;
		}

		50%,
		100% {
			box-shadow: 0 0 200rpx #03e9f4,
				0 0 50rpx #03e9f4,
				0 0 25rpx #03a9f4,
				0 0 5rpx #03a9f4;
		}
	}

	.form-images {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		border-top-left-radius: 30rpx;
		border-top-right-radius: 30rpx;
	}

	.contrast {
		height: 180rpx;
		width: 180rpx;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		/* border: 1rpx solid red */

	}

	.contrast-image {
		width: 100%;
	}
	.container-image{
		cursor: pointer;
		/* border: 1rpx solid red; */
		z-index: 999;
	}
	.image-left{
		border-top-left-radius: 30rpx;
	}
	.image-right{
		border-top-right-radius: 30rpx;
	}
	.contrast-image:nth-child(1) {
		
	}
	.contrast-image:nth-child(2) {
		
	}
	
	.right-icon {}

	.form-Info {
		flex-grow: 1;
		width: 100%;
		/* border: 1rpx blue solid; */
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		position: relative;
		margin-top: 10rpx;
		/* align-items: center; */
		padding-top: 60rpx;

	}

	.info {
		color: #fff;
		font-family: sans-serif;
		font-size: 24rpx;
		/* border: 1rpx red solid; */
		width: 90%;
		height: 110rpx;
		margin-top: 40rpx;
		padding: 8rpx 4rpx;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		background: rgba(0, 0, 0, 0.021);
		border-radius: 15rpx;
		position: relative;
		transform: 0.5s;
		overflow: hidden;

	}

	.info:nth-last-child(1) {
		margin-bottom: 40rpx;
	}

	/* .info:hover{
		
	}	
	.info span{
		position: absolute;
		display: block;
		overflow: hidden;
	}
	.info:nth-child(1){
		filter: hue-rotate(200deg);
	}
	.info span:nth-child(1){
		top: 0;
		left: 0;
		width: 100%;
		height: 4rpx;
		background: linear-gradient(90deg ,transparent,#03e9f4);
		animation: animate1 5s linear infinite;
	}
	.info span:nth-child(2) {

			top: -100%;

			right: 0;

			width: 4rpx;

			height: 100%;

			background: linear-gradient(180deg, transparent, #03e9f4);

			animation: animate2 5s linear infinite;

			animation-delay: 2.2s;

		}

	

	.info span:nth-child(3) {

			bottom: 0;

			right: -100%;

			width: 100%;

			height: 4rpx;

			background: linear-gradient(270deg, transparent, #03e9f4);

			animation: animate3 5s linear infinite;

			animation-delay: 3.4s;

		}

	

	.info span:nth-child(4) {

			bottom: -100%;

			left: 0;

			width: 4rpx;

			height: 100%;

			background: linear-gradient(360deg, transparent, #03e9f4);

			animation: animate4 5s linear infinite;

			animation-delay: 4.6s;

		}


	 */
	.info-content {
		width: 95%;
		height: 95%;
		background: rgba(255, 255, 255, 0.121);
		display: flex;
		flex-direction: row;
		align-items: center;
		border-radius: 15rpx;
		padding-left: 12rpx;
	}

	.info-date {
		position: absolute;
		top: 0;
		width: 100%;
		display: flex;
		flex-direction: column;
		/* border-top: 10rpx dotted red; */
		/* border: 1rpx blue solid; */
		justify-content: flex-end;
		align-items: flex-end;
		padding: 10rpx 0rpx;
		color: #fff;
		font-family: sans-serif;
		font-size: 24rpx;
	}

	.info-date>text {
		font-weight: 600;
		padding: 5rpx 15rpx;
	}

	.info-content>text:nth-child(1) {
		font-weight: 600;
		padding: 0 4rpx;
	}

	.info-content>text:nth-child(2) {
		flex-wrap: wrap;

	}

	.info-res {}

	.info-advice {}

	.info-again {}
</style>