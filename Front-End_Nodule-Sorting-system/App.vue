<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
			uni.setStorage({
				key:'showImage',
				data:'http://5646ff0f.r17.cpolar.top/showImage/'
			})
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	.uni-tabbar{
		z-index: 9999;
	}
</style>
