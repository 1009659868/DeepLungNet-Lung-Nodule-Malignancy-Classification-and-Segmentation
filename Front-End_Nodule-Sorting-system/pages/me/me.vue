```css
<template>	
	<view>
		<sideBar></sideBar>
		<view class="background"></view>
		
		<div class="childcontainer">
			<ul class="main">
				<!-- 试着插入了几个图片感觉都不是很协调,后面可以再调一下 -->
                <!-- 主要问题在于每张图片的色彩不统一,导致页面看起来杂乱 -->
				<!-- 然后就是整个app的配色问题,个人觉得尽量都采用同一色系或者是渐进的,体现出层次感,mycolor.space可以根据某种颜色自动配色-->
				<!-- 这里用的是mycolor.sapce的自动颜色配色 -->
				<li>
					<div class="image" style="background-color: #97caff;">
						<!-- <img src="/static/window-shades/_检查报告.png" alt="" /> -->
					</div>
					<div class="flag"><a href="#">检查报告</a></div>
				</li>
				<li>
					
					<div class="image" style="background-color: #6A9FD1;">
					<!-- 	<img src="/static/window-shades/feedback.png" alt="" /> -->
					</div>
					<div class="flag"><a href="#">反馈</a></div>
				</li>
				<li>
					<div class="image" style="background-color: #3D76A6;">
						<!-- <img src="/static/window-shades/个人信息.png" alt="" /> -->
					</div>
					<div class="flag"><a href="#">个人信息</a></div>
				</li>
				
				<li>
					<div class="image" style="background-color: #39a7e2;">	</div>
					<div class="flag"><a href="#">收藏</a></div>
				</li>
				<li>
					<div class="image" style="background-color: #004F7C;">	
					<!-- <img src="/static/window-shades/患者关注.png" alt="" /> -->
					</div>
					<div class="flag"><a href="#">患者关注</a></div>
				</li>
				
				
			</ul>
		</div>
	</view>
</template>

<script>
	import sideBar from "../../components/sideBar.vue"
	export default {
		components:{
			sideBar
		},
		data() {
			return {
				title: 'Hello',
				username:"GGB",
				public:"kk"
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
.childcontainer{
	/*距离组件右边缘200px*/
	/* margin-left: 200rpx; */
}
*{
	margin: 0rpx;
	padding: 0rpx;
}
ul,ol{
	list-style: none;
}
.main{
	width: 1200rpx;
	height: 600rpx;
	margin: 150rpx auto;
	overflow: hidden;
	/* border:1px solid  red; */
}
li{
	width: 160rpx;
	float: left;/*图片在同一排*/
	position: relative;/*相对定位*/
	transition: all 1s;/*过渡时间为1s*/
}
.image{
	width: 600rpx;
	height: 420rpx;
	/* border:1px solid #FFFFFF *//*设置div的宽高*/
}
.image img{
	/* width: 100%;
	height: 100%; */
	object-fit: cover;/*让每张图片占满div*//*自适应*/
}
/*文字所在的div*/
.flag{
	position: absolute;
	left: 0rpx;
	bottom: 0rpx;
	width: 100%;
	height: 60rpx;
	line-height: 60rpx;
	text-align: center;
	color: #FFFFFF;
	background:rgba(0, 0, 0, 0.25);
}
/*悬停在main上时,列表项被设置成100px*/
.main:hover li {
	width: 100rpx;
	/* border:2px solid green; */
	
}
/*悬停在li上时,列表项被设置成600px*/
.main li:hover{
	width: 600rpx;
}
a{
	text-decoration: none;
	font-style: initial;
	color: #FFFFFF;
}
</style>

```

