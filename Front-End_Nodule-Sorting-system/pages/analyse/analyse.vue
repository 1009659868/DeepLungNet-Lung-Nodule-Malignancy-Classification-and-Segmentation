<template>
	<view>
		<sideBar></sideBar>
		<view class="background"></view>
		<view>
			<image src="../../static/output.png" style="width: 100%;" mode="widthFix"></image>
		</view>
	</view>
</template>

<script>
	import sideBar from '../../components/sideBar.vue'
	export default {
		components:{
			sideBar
		},
		data() {
			return {
				
			}
		},
		methods: {
			
		}
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
</style>
