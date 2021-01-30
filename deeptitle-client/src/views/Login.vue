

<template>
	<div>

		<v-toolbar dark prominent src="../assets/code.jpg" style="-webkit-user-select: none;-webkit-app-region: drag">
			<v-toolbar-title>DeepTitle Tool</v-toolbar-title>
			<v-spacer></v-spacer>
			<v-btn style="-webkit-app-region: no-drag" icon @click.native.stop="winControl('minimize')">
				<v-icon>remove</v-icon>
			</v-btn>
			<v-btn style="-webkit-app-region: no-drag" icon @click.native.stop="winControl('close')">
				<v-icon>close</v-icon>
			</v-btn>
		</v-toolbar>
		<!-- <v-container class="white lighten-3" fill-height="100%"> -->
		<v-card width="100%" flat>
			<v-card-title class="title font-weight-regular text-center">
				<span>Choose the background service you need</span>
			</v-card-title>
			<v-card-text>
				<v-row justify="center">
					<v-radio-group v-model="network"  row>
					      <v-radio
					        label="Localhost"
					        value="http://127.0.0.1:5000"
					      ></v-radio>
					      <v-radio
					        label="Internet"
					        value="http://ntuyg.natapp1.cc"
					      ></v-radio>
					</v-radio-group>
				</v-row>
				<v-row class="mt-4 ma-4" justify="center">
					<v-btn block dark elevation="4" color="black lighten-10" depressed @click="submitLogin" :loading="loading2" :disabled="loading2">
						Try
						<template v-slot:loader>
							<span class="blue--text">Loading...</span>
						</template>
					</v-btn>
				</v-row>
			</v-card-text>
		</v-card>
		<v-dialog  v-model="show" persistent width="500">
			<v-card>
				<v-card-title class="headline grey lighten-2">
					Failed
				</v-card-title>
				<v-card-text>
					Network connection failed! 
					If it is a local background service, please check whether the service is started. 
					If it is an Internet service, please contact the administrator 74621980@qq.com
				</v-card-text>
				<v-divider></v-divider>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="primary" text @click="show = false">
						Close
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</div>
</template>

<script>
	const ipcRenderer = require('electron').ipcRenderer;
	import axios from 'axios'
	export default {
		data: () => ({
			loader: null,
			loading2: false,
			network: "http://127.0.0.1:5000",
			show: false
		}),
		watch: {
		},
		computed: {
		},
		methods: {
			submitLogin() {
				this.loader = 'loading2'
				axios.get(this.network + '/hello').then(res => {
					console.log(res)
				      if(res == 'Hello World'){
						  window.sessionStorage.setItem('net', this.network)
					
						  this.$router.push({
						  	name: 'Home'
						  })
						  ipcRenderer.send('changeSize')
					  } else {
						  this.show=true;
					  }
				}).catch(res => {
					this.show=true;
				})
				this.loader = null
			},
			// 窗口最小化、关闭
			winControl(action) {
				switch (action) {
					case 'minimize':
						ipcRenderer.send('window-min')
						break;
					case 'close':
						ipcRenderer.send('window-close')
						break;
					default:
						break;
				}
			}
		}
	}
</script>

<style>
	.custom-loader {
		animation: loader 1s infinite;
		display: flex;
	}

	@-moz-keyframes loader {
		from {
			transform: rotate(0);
		}

		to {
			transform: rotate(360deg);
		}
	}

	@-webkit-keyframes loader {
		from {
			transform: rotate(0);
		}

		to {
			transform: rotate(360deg);
		}
	}

	@-o-keyframes loader {
		from {
			transform: rotate(0);
		}

		to {
			transform: rotate(360deg);
		}
	}

	@keyframes loader {
		from {
			transform: rotate(0);
		}

		to {
			transform: rotate(360deg);
		}
	}
</style>

<style>
	html {
		/* 禁用html的滚动条，因为用的无框架窗口，默认就会有一个滚动条，所以去掉 */
		overflow-y: hidden;
	}

	/*定义滚动条高宽及背景 高宽分别对应横竖滚动条的尺寸*/
	/* ::-webkit-scrollbar {
		width: 2px;
	}
 */
	/*定义滚动条轨道 内阴影+圆角*/
	::-webkit-scrollbar-track {}

	/*定义滑块 内阴影+圆角*/
	/* ::-webkit-scrollbar-thumb {
		border-radius: 99px;
	} */
</style>
