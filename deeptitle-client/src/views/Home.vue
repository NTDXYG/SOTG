<template>
	<div>
		<v-system-bar color="white" window app style="-webkit-app-region: drag">
			<v-icon>mdi-home</v-icon>
			<span>DeepTitle Tool</span>
			<v-spacer></v-spacer>
			<div style="-webkit-app-region: no-drag">
				<v-icon @click.native.stop="winControl('minimize')">mdi-minus</v-icon>
				<v-icon class="ml-6" @click.native.stop="winControl('maximize')" v-show="winFlag">mdi-checkbox-blank-outline</v-icon>
				<v-icon class="ml-6" @click.native.stop="winControl('maximize')" v-show="!winFlag">mdi-dock-window</v-icon>
				<v-icon class="ml-6" @click.native.stop="winControl('close')">mdi-close</v-icon>
			</div>
		</v-system-bar>

		<v-app>
			<v-navigation-drawer :mini-variant="drawer" app permanent>
				<template v-slot:prepend>
					<v-img :aspect-ratio="16/9" src="../assets/code.jpg">
						<div class="d-flex flex-column">
							<v-list-item class="px-2" dark>
								<v-list-item-avatar>
									<v-menu top offset-x>
										<template v-slot:activator="{ on, attrs }">
											<!-- <v-img v-bind="attrs" v-on="on" src="https://randomuser.me/api/portraits/men/85.jpg"></v-img> -->
											<v-icon large v-bind="attrs" v-on="on">mdi-account-box</v-icon>
										</template>
										<v-list>
											<v-list-item @click="goLoginPage()">
												<v-list-item-title>exit</v-list-item-title>
											</v-list-item>
										</v-list>
									</v-menu>
								</v-list-item-avatar>
								<v-list-item-title>User</v-list-item-title>
								<v-btn icon @click.stop="drawer = !drawer">
									<v-icon>mdi-chevron-left</v-icon>
								</v-btn>
							</v-list-item>
						</div>
					</v-img>

				</template>

				<v-divider class="mb-2" />
				<template v-slot:append>
					<div class="pa-2">
						<v-btn block v-show="!drawer" @click="dialog = true">
							<v-icon left>
								mdi-information-outline
							</v-icon>
							About
						</v-btn>
						<v-icon v-show="drawer" class="ma-2" @click="dialog = true">
							mdi-information-outline
						</v-icon>
					</div>
				</template>
			</v-navigation-drawer>
			<v-main>
				<router-view></router-view>
			</v-main>

		</v-app>
		<v-dialog v-model="dialog" width="500">
			<v-card>
				<v-card-title class="headline grey lighten-2">
					About
				</v-card-title>
				<v-card-text>
					Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
					magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
					consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
					Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
				</v-card-text>
				<v-divider></v-divider>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="primary" text @click="dialog = false">
						Close
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</div>
</template>

<script>
	const ipcRenderer = require('electron').ipcRenderer

	export default {
		data: () => ({
			currentRouteName: null,
			dialog: false,
			drawer: null,
			name: 'Home',
			winFlag: true,
			menuList: [{
					name: 'Main',
					icon: 'mdi-home-circle',
					cname: 'Main',
					active: false,
				}
			],
		}),


		mounted() {

			this.changeTab("Main")
			this.currentRouteName = "Main"
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
			goLoginPage() {
				this.$router.push({
					name: 'Login'
				})
				ipcRenderer.send('defaultSize')
			},
			//窗口最大化、最小化、关闭
			winControl(action) {
				switch (action) {
					case 'minimize':
						ipcRenderer.send('window-min')
						break;
					case 'maximize':
						ipcRenderer.send('window-max', {
							winFlag: this.winFlag
						})
						this.winFlag = !this.winFlag
						break;
					case 'close':
						ipcRenderer.send('window-close')
						break;
					default:
						break;
				}
			},
		}
	}
</script>
