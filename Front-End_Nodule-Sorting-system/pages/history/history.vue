<template>
	<view :style="temp" class="body">
		
		<view class="container">
			<view class="content">
				<div class="void" id="void">
					<div class="crop">
						<ul class="card-list" style="--count:6;">
							<li>
								<div class="card">
									<a href="#">
										<div>2025-5-1</div>
										<div>4.中度可疑(62.4574%)</div>
										<div>加强健康监测，定期进行体检，并注意任何异常症状。</div>
									</a></div>
							</li>
							<li>
								<div class="card">
									<a href="#">
										<div>2025-5-1</div>
										<div>4.中度可疑(61.9601%)</div>
										<div>加强健康监测，定期进行体检，并注意任何异常症状。</div>
									</a></div>
							</li>
							<li>
								<div class="card">
									<a href="">
										<div>2025-5-1</div>
										<div>2.中度不太可能(68.0149%)</div>
										<div>保持定期体检，及时发现任何健康问题并寻求医疗建议。</div>
									</a></div>
							</li>
							<li>
								<div class="card">
									<a href="#">
										<div>2025-5-1</div>
										<div>3.不确定的(58.3203%)</div>
										<div>积极争取更多的健康信息，寻求专业医生的建议，并进行必要的检查。</div>
									</a></div>
							</li>
							<li>
								<div class="card"><a href="#">
										<div>2025-5-2</div>
										<div>4.中度可疑(88.5037%)</div>
										<div>加强健康监测，定期进行体检，并注意任何异常症状。</div>
									</a></div>
							</li>
							<li>
								<div class="card"><a href="#">
										<div>2025-5-2</div>
										<div>2.中度不太可能(99.6798%)</div>
										<div>保持定期体检，及时发现任何健康问题并寻求医疗建议。</div>
									</a></div>
							</li>
						</ul>
						<div class="last-circle"></div>
						<div class="second-circle"></div>
					</div>
					<div class="mask" @mousedown="speedUp()" @mouseup="speedDown()" @touchstart="speedUp()" @touchend="speedDown()"></div>
					<div class="center-circle"></div>
				</div>
				
			</view>
			<sideBar></sideBar>
		</view>
		
		<view class="backgorund"></view>
	</view>
	
</template>

<script>
	import sideBar from '../../components/sideBar.vue'
	export default {
		components: {
			sideBar
		},
		data() {
			return {
				temp:{
					'--rotate-speed': 40,
					'--count': 8,
					'--easing': 'cubic-bezier(0.000, 0.37, 1.000, 0.63)',
				}
				
			}
		},
		methods: {
			speedUp(){
				this.temp['--rotate-speed']=5
			},
			speedDown(){
				this.temp['--rotate-speed']=40
			}
		}
	}
</script>

<style lang="scss">
	/* 定义全局变量 */
	page {
		display: flex;
		flex-direction: column;
		height: 100%;
	}
	/* 设置页面样式 */
	.body {
		height: 100%;
		// border: 1rpx solid red;
	}
	.backgorund {
		position: fixed;
		top: 0;
		left: 0;
		z-index: 0;
		width: 100%;
		height: 100%;
		background-color: aquamarine;
	}
	.container{
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.2);
		z-index: 1;
		position: relative;
	}
	.content{
		width: 100%;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		z-index: 2;
	}
	/* 设置容器样式 */
	.void {
		width: 100%;
		max-width: 1024rpx;
		margin: auto;
		position: relative;
		aspect-ratio: 1 / 1;
		// border: 1rpx solid red;
		z-index: 3;
	}

	/* 鼠标悬停时暂停动画 */
	ul:hover * {
		animation-play-state: paused;
	}

	/* 设置列表样式 */
	ul {
		list-style-type: none;
		margin: 0;
		padding: 0;
		position: relative;
		width: 100%;
		aspect-ratio: 1 / 1;
		z-index: 3;
		transition: 0.5s;
	}

	/* 设置列表项样式 */
	li {
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		width: 100%;
		animation: rotateCW calc(var(--rotate-speed) * 1s) var(--easing) infinite;
	}

	/* 设置卡片样式 */
	.card {
		width: 27%;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		padding: 16rpx 24rpx;
		gap: 8rpx;
		background: #FFFFFF;
		box-shadow: 0rpx 4rpx 12rpx rgba(70, 0, 255, 0.1), 0px 16px 32px rgba(165, 135, 255, 0.1);
		border-radius: 12rpx;
		font: 400 14rpx '';
		color: #535062;
		animation: rotateCCW calc(var(--rotate-speed) * 1s) var(--easing) infinite;
		overflow: hidden;
	}
	.card>div{
		width: 100%;
	}

	/* 设置图片样式 */
	.card img {
		width: 100%;
	}

	/* 设置链接样式 */
	a {
		text-decoration: none;
		color: unset;
		display: block;
		height: 85rpx;
		width: 100%;
	}

	/* 设置模型名称样式 */
	.model-name {
		font-weight: 500;
		font-size: 18rpx;
		line-height: 150%;
		color: #3B2ED0;
		display: block;
	}

	/* 设置SVG样式 */
	svg {
		position: absolute;
		top: 0;
		left: 0;
		z-index: 0;
	}

	/* 设置不同列表项的动画延迟 */
	li:nth-child(2),
	li:nth-child(2) .card {
		animation-delay: calc((var(--rotate-speed)/var(--count)) * -1s);
	}

	li:nth-child(3),
	li:nth-child(3) .card {
		animation-delay: calc((var(--rotate-speed)/var(--count)) * -2s);
	}

	li:nth-child(4),
	li:nth-child(4) .card {
		animation-delay: calc((var(--rotate-speed)/var(--count)) * -3s);
	}

	li:nth-child(5),
	li:nth-child(5) .card {
		animation-delay: calc((var(--rotate-speed)/var(--count)) * -4s);
	}

	li:nth-child(6),
	li:nth-child(6) .card {
		animation-delay: calc((var(--rotate-speed)/var(--count)) * -5s);
	}

	/* 定义顺时针旋转动画 */
	@keyframes rotateCW {
		from {
			transform: translate3d(0px, -50%, -1px) rotate(-45deg);
		}

		to {
			transform: translate3d(0px, -50%, 0px) rotate(-315deg);
		}
	}

	/* 定义逆时针旋转动画 */
	@keyframes rotateCCW {
		from {
			transform: rotate(45deg);
		}

		to {
			transform: rotate(315deg);
		}
	}

	/* 设置中心圆样式 */
	.center-circle {
		position: absolute;
		width: 230rpx;
		aspect-ratio: 1 / 1;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
		background: #FFFFFF;
		box-shadow: 0rpx 18rpx 36rpx -18rpx rgba(12, 5, 46, 0.3),
			0rpx 3r0px 60rpx -12rpx rgba(12, 5, 46, 0.25);
		border-radius: 50%;
		background-size: cover;
		background-position: -35rpx 0;
	}

	/* 设置第二个圆样式 */
	.second-circle {
		position: absolute;
		width: 40%;
		aspect-ratio: 1 / 1;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
		background: #F5F4FE;
		opacity: 0.5;
		box-shadow: 0rpx 18rpx 36rpx -18rpx rgba(12, 5, 46, 0.3),
			0rpx 30rpx 60rpx -12rpx rgba(12, 5, 46, 0.25);
		border-radius: 50%;
		/* background-image: url(./03.gif); */
	}

	/* 设置最后一个圆样式 */
	.last-circle {
		position: absolute;
		width: 66%;
		aspect-ratio: 1 / 1;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
		background: #F5F4FE;
		opacity: 0.25;
		box-shadow: 0rpx 18rpx 36rpx -18rpx rgba(12, 5, 46, 0.3), 0rpx 30rpx 60rpx -12rpx rgba(12, 5, 46, 0.25);
		border-radius: 50%;
		/* background-image: url(./03.gif); */
	}

	/* 设置裁剪样式 */
	.crop {
		// border: 1rpx solid black;
		-webkit-mask-image: linear-gradient(90deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0) 50%,
				rgba(0, 0, 0, 1) 50%, rgba(0, 0, 0, 1));
	}

	/* 设置遮罩样式 */
	.mask {
		position: absolute;
		top: 0;
		left: 0;
		bottom: 0;
		width: 50%;
		background-position: 100% 50%;
		background-repeat: no-repeat;
		background-image: radial-gradient(100% 50% at 100% 50%, rgba(60, 26, 229, 0.25) 0%,
				rgba(59, 26, 229, 0.241896) 20%,
				rgba(53, 26, 229, 0.1872) 40%,
				rgba(41, 23, 240, 0.104) 60%,
				rgba(34, 26, 229, 0.0184296) 90%, rgba(32, 26, 229, 0) 100%);
		// border: 1rpx solid red;
	}

	/* 设置遮罩样式后的效果 */
	.mask:after {
		content: "";
		position: absolute;
		width: 1rpx;
		height: 100%;
		right: 0;
		display: block;
		background-image: linear-gradient(180deg, rgba(60, 26, 229, 0) 0%, #3C1AE5 50%,
				rgba(60, 26, 229, 0) 100%);
	}
</style>