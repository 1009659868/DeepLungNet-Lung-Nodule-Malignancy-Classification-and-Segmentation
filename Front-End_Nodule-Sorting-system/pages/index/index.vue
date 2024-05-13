```vue

<template>
	<view style="background-color: white;">
		<sideBar></sideBar>
		<view class="background"></view>
		<!-- poker组件需要传入背景图片,标题,跳转地址,以及位置下标 -->
		<!-- 具体poker样式可以在poker组件的卡片样式处修改 -->
		<view class="mask"></view>
		<poker :pokerInfo="pokerInfo"></poker>


	</view>
</template>

<script>
	import sideBar from '../../components/sideBar.vue'
	import poker from '../../components/poker/poker.vue'
	export default {
		components: {
			sideBar,
			poker
		},
		data() {
			return {
				poker: null,
				pokerInfo: [{
					pokerIndex: 0,
					pokerImagePath: '/static/photos/photo (0).webp',
					pokerTitle: '诊断',
					pokerNavgateTo: '../../pages/mainFunction/mainFunction',
					
				}, {
					pokerIndex: 1,
					pokerImagePath: '/static/photos/photo (1).webp',
					pokerTitle: '历史',
					pokerNavgateTo: '../../pages/history/history',
				}, {
					pokerIndex: 2,
					pokerImagePath: '/static/photos/photo (2).webp',
					pokerTitle: '分析',
					pokerNavgateTo: '../../pages/analyse/analyse',
				}, {
					pokerIndex: 3,
					pokerImagePath: '/static/photos/photo (3).webp',
					pokerTitle: '我的',
					pokerNavgateTo: '../../pages/me/me',
				}, {
					pokerIndex: 4,
					pokerImagePath: '/static/photos/photo (4).webp',
					pokerTitle: '设置',
					pokerNavgateTo: '../../pages/setting/setting',
				},
				],
				imgs: [],

			};
		},
		onLoad() {

		},
		mounted() {

		},
		methods: {

		}
	}
</script>

<style scoped>
	div {
		user-select: none;
	}

	page {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
		background-color: #000;
	}

	.background {
		position: fixed;
		top: 0;
		left: 0;
		z-index: 0;
		width: 100%;
		height: 100%; 
		/* background-color: aquamarine; */
		background-color: aquamarine;
	}
	.mask{
		position: fixed;
		top: 0;
		left: 0;
		z-index: 1;
		width: 100%;
		height: 100%; 
		/* background-color: aquamarine; */
		background-color: rgba(0, 0, 0, 0.2);
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
		z-index: 10;
	}

	/* 右下角光圈 */
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
		z-index: 10;
	}
</style>




```