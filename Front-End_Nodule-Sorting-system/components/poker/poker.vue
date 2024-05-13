<template>
	<view>
		<div class="container">
			<div class="poker poker1" @click="goSb(pokerInfo[0])" >
				<div class="poker-content">
					{{pokerInfo[0].pokerTitle}}
				</div>
				<div class="poker-img">
					<image :src="pokerInfo[0].pokerImagePath" mode="widthFix"></image>
				</div>

			</div>
			<div class="poker poker2" @click="goSb(pokerInfo[1])">
				<div class="poker-content">
					{{pokerInfo[1].pokerTitle}}
				</div>
				<div class="poker-img">
					<image :src="pokerInfo[1].pokerImagePath" mode="widthFix"></image>
				</div>

			</div>
			<div class="poker poker3" @click="goSb(pokerInfo[2])">
				<div class="poker-content">
					{{pokerInfo[2].pokerTitle}}
				</div>
				<div class="poker-img">
					<image :src="pokerInfo[2].pokerImagePath" mode="widthFix"></image>
				</div>
			</div>
			<div class="poker poker4" @click="goSb(pokerInfo[3])">
				<div class="poker-content">
					{{pokerInfo[3].pokerTitle}}
				</div>
				<div class="poker-img">
					<image :src="pokerInfo[3].pokerImagePath" mode="widthFix"></image>
				</div>
			</div>
			<div class="poker poker5" @click="goSb(pokerInfo[4])">
				<div class="poker-content">
					{{pokerInfo[4].pokerTitle}}
				</div>
				<div class="poker-img">
					<image :src="pokerInfo[4].pokerImagePath" mode="widthFix"></image>
				</div>
			</div>
			<div class="poker_top poker5 pokermove" @click="move">
				<div class="poker-content">
					Next
				</div>
				<div class="poker-img">
					<image src="#" mode="widthFix" ></image>
				</div>

			</div>
		</div>
	</view>
</template>

<script>
	export default {
		name: "poker",
		props: ["pokerInfo"],
		data() {
			return {
				poker: null,
				clickNum:{
					"0":0,
					"1":0,
					"2":0,
					"3":0,
					"4":0,
				}
			};
		},
		mounted() {
			console.log(this.pokerInfo.value)
			console.log("init");

			const poker = {
				imgs: [],
				img_index: 0,
				poker_eles: {},
				transform_datas: [
					"rotate(-30deg)",
					"rotate(-15deg) translate(38%, -12%)",
					"rotate(-0deg) translate(80%, -30%)",
					"rotate(15deg) translate(105%, -50%)",
					"rotate(30deg) translate(120%, -23%)",
				],
				transform_selected: [
					"rotate(-15deg) translate(-10%, -50%)",
					"rotate(-2deg) translate(10%, -55%)",
					"rotate(15deg) translate(30%, -80%)",
					"rotate(-10deg) translate(120%, -68%)",
					"rotate(30deg) translate(120%, -23%)",
				],
				init() {
					for (let i = 0; i < 6; i++) {
						let img = new Image();
						img.src = `/static/photos/photo (${i}).webp`;
						this.imgs.push(img);
					}
					this.poker_eles = [...document.getElementsByClassName("poker")];
					this.poker_eles.forEach((obj, index) => {
						// console.log("---")
						// console.log("obj:"+obj.nums)
						// console.log("index:"+index)
						// console.log("---")
						obj.nums = index;
					});

					// this.img_index = this.poker_eles.length;
					this.img_index = 0;
					console.log("init suc");
				},
				move() {
					for (let key in this.clickNum) {
						this.clickNum[key] = 0;
					}
					this.poker_eles.map((ele) => {
						let nums = ele.nums;
						// console.log("*******************")
						// console.log("num:"+nums)
						// console.log("poker_eles.length:"+this.poker_eles.length)
						if (nums + 1 >= this.poker_eles.length) {
							nums = 0;
							ele.style.transition = "";
							// ele.querySelector("img").src =
							// 	this.imgs[this.img_index].src;
							// this.img_index++;
							// if (this.img_index >= this.imgs.length)
							// 	this.img_index = 0;
						} else {
							nums += 1;
							ele.style.transition = "transform 0.3s ease";
						}
						// console.log("num:"+nums)
						// console.log("poker_eles.length:"+this.poker_eles.length)
						// console.log("*******************")
						ele.style.zIndex = nums;
						ele.style.transform = this.transform_datas[nums];
						ele.nums = nums;
						
					});
				},
			};
			this.poker = poker;
			this.poker.init();

		},
		methods: {
			move() {
				// 调用 poker 对象的 move 方法
				this.poker.move();
			},
			goSb(pokerInfo) {
				// 假设 pokerInfo.pokerIndex 是一个合法的索引值
				const index = pokerInfo.pokerIndex;
				// 遍历对象的属性，将每个属性的值都设为 0
				for (let key in this.clickNum) {
					if(key!=index)
					this.clickNum[key] = 0;
				}
				
				
				// 遍历 poker_eles 数组，对每个元素设置对应的 transform
				this.poker.poker_eles.map((ele, i) => {
				  // 设置当前元素的 transform
				  let nums = ele.nums;
				  ele.style.transform = (i === index) ? this.poker.transform_selected[nums] : this.poker.transform_datas[nums];
				});
				this.clickNum[pokerInfo.pokerIndex]+=1
				if(this.clickNum[pokerInfo.pokerIndex]>=2){
					for (let key in this.clickNum) {
						this.clickNum[key] = 0;
					}
					// 遍历 poker_eles 数组，对每个元素设置对应的 transform
					this.poker.poker_eles.map((ele, i) => {
					  // 设置当前元素的 transform
					  let nums = ele.nums;
					  ele.style.transform = this.poker.transform_datas[nums];
					});
					
					// 尝试使用 switchTab 导航到目标页面
					uni.switchTab({
						url: pokerInfo.pokerNavgateTo
					}).then(() => {
						// 如果成功跳转到目标页面，则不执行下面的代码
						console.log('成功跳转到目标页面');
					}).catch(() => {
						// 如果 switchTab 失败，则使用 navigateTo 导航到目标页面
						console.log('无法使用 switchTab，使用 navigateTo 导航到目标页面');
						uni.navigateTo({
							url: pokerInfo.pokerNavgateTo
						});
					});

				}
				
				
				

			}

		}
	}
</script>

<style scoped>
	div {
		user-select: none;
	}
	/* 容器样式 */
	.container {
		position: relative;
		width: 720rpx;
		height: 720rpx;
		margin-bottom: 8rpx;
		z-index: 3;
		/* border: 1px solid red; */

	}
	/* 卡片样式 */
	.poker,
	.poker_top {
		position: absolute;
		width: 250rpx;
		height: 325rpx;
		border: 3.6rpx solid #fff;
		border-radius: 24rpx;
		background-color: #17f700;
		/* transform-origin: bottom left; */
		overflow: hidden;
		top: 30%;
		left: 12%;
		transition: .5s;
	}
	/* 卡片内容样式 */
	.poker-content {
		height: 100%;
		width: 100%;
		position: absolute;
		top: 0;
		z-index: 10;
	}
	/* 卡片背景图片容器 */
	.poker-img {
		height: 100%;
		width: 100%;
		position: absolute;
		top: 0;
		z-index: 1;

	}
	/* 卡片背景图片 */
	.poker-img image {
		position: relative;
		width: 100%;
	}

	.poker_top {
		background-color: #fff;
		transition: 0.3s ease;
		cursor: pointer;
		z-index: 1000;
	}

	.poker_top:hover {
		background-color: #aaa;
	}

	.poker1 {
		transform: rotate(-10deg) ;
	}

	.poker2 {
		transform: rotate(-6deg) translate(35%, -12%);
	}

	.poker3 {
		transform: rotate(-2deg) translate(65%, -19%);
	}

	.poker4 {
		transform: rotate(2deg) translate(95%, -26%);
	}

	.poker5 {
		transform: rotate(30deg) translate(120%, -23%);
	}
</style>