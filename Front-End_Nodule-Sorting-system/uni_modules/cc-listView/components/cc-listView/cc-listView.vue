<template>

	<view>

		<view class="uni-list-cell" hover-class="uni-list-cell-hover" v-for="(item, index) in productList"
			:key="item.id" @click="goProDetail(item)">
		
		
			<view class="topTitleV">{{item.proName}}</view>
			<view class="topTitleV unitV">{{item.proUnit}}</view>
			
			<view
				style="display: flex; flex: 1; flex-wrap: wrap; margin-top: 0px; margin-left: -8px; height: 38px; width:calc(100vw-62px)">
		
				<!-- 自定义了一个data-id的属性,可以通过js获取到它的值!  hover-class 指定按下去的样式类-->
				<view class="cellView" :style="{ color: bindColor(index), backgroundColor: bindBgColor(index) }"
					v-for="(tagItem, index) in bindTag(item)" :key="index">
					{{tagItem}}
				</view>
		
		
			</view>
		
		
		</view>

	</view>

</template>

<script>
	export default {
		props: {

			productList: {
				type: Array,
				default(){
					return []
				}
			}
			
			

		},
		data() {
			return {

			}
		},
		methods: {
			goProDetail(item) {

				this.$emit('click', item)
			},
			bindTag(item) {
			
				return [item.area, item.proType, item.stage]
			},
			bindColor(index) {
				let colorArr = ['#4473FF', '#FFA01B', '#41D380'];
				return colorArr[index % 3];
			},
			bindBgColor(index) {
				let bgColorArr = ['#F1F4FA', '#FFF5E8', '#ECFAF2'];
				return bgColorArr[index % 3];
			},

		}
	}
</script>

<style scoped>
	.uni-list-cell {
		flex-direction: column;
		margin-top: 10px;
		background-color: white;
		padding: 6px 12px;
	
	
	}
	
	.topTitleV {
	
		height: 26px;
		line-height: 26px;
		color: #333333;
		font-family: PingFangSC-Semibold, PingFang SC;
		font-weight: 500;
		font-size: 14px;
		
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	
	}
	.unitV{
		color: #555555;
		font-size: 12px;
		margin-top: 0px;
		font-family: PingFangSC-Regular, PingFang SC;
		
	}
	
	.cellView {
		margin-top: 8px;
		margin-left: 8px;
		height: 22px;
		line-height: 22px;
		text-align: center;
		border-radius: 2px;
		padding: 0px 4px !important;
		font-size: 12px;
	
		color: #4272FF;
		background: #F3F4F6;
	}
	
</style>