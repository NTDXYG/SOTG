<template>
	<v-card tile flat>
		<v-sheet id="scrolling-techniques-4" class="overflow-y-auto" max-height="100vh">
			<v-parallax height="200" dark src="../../assets/network.jpg">
				<v-row align="center" justify="center">
					<v-col class="text-center" cols="12">
						<h1 class="display-1 font-weight-thin mb-4">
							DeepTitle<span class="blue--text">2</span>Tool
						</h1>
						<h3 class="subheading">
							DeepTitle: xxxxxx
						</h3>
					</v-col>
				</v-row>
			</v-parallax>
			<router-view></router-view>
		</v-sheet>
	</v-card>

</template>

<script>
	export default {

		components: {},

		data: () => ({

			menuList: [{
				name: 'Title Generation',
				cname: 'Page',
			}],

		}),

		computed: {},

		created() {},

		mounted() {
			this.changeTab("Page")
			this.currentRouteName = "Page"
		},

		methods: {

			changeTab(name) {
				if (name != this.currentRouteName) {
					this.$router.replace({
						name: name
					})
					this.currentRouteName = name;
				} else {
					console.log('请勿跳转当前的路由')
				}
			},





		}
	}
</script>

<style>
</style>
