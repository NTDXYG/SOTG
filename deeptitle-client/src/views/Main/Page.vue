<template>
	<div>
		<v-card class="d-flex justify-center align-center" color="grey lighten-5" flat tile height="88vh">
			<v-card class="align-self-start" tile flat color="grey lighten-5" width="40vw">
				<h3 class="ma-4 text-center">CODE</h3>
				<v-card class="ma-2 white" elevation="12">
					<v-card-text>
						<codemirror v-model="code" :options="options"></codemirror>

						<v-divider class="my-5"></v-divider>
						<v-textarea height="22vh" solo name="input-7-4" v-model="describe" label="Describe"></v-textarea>
					</v-card-text>
				</v-card>
			</v-card>
			<v-btn fab dark large color="orange" class="mx-10 mt-16 align-self-start">
				<v-icon @click="requestData" dark large>mdi-arrow-right-bold-outline</v-icon>
			</v-btn>
			<v-card class="align-self-start" outlined tile width="40vw" color="grey lighten-5">
				<h3 class="ma-4 text-center">Result</h3>
				<v-card class="ma-2" elevation="12" :loading="loading">
					<template slot="progress">
						<v-progress-linear color="yellow darken-2" height="6" indeterminate></v-progress-linear>
					</template>
					<v-card-text>
						<v-sheet class="overflow-y-auto" id="scrolling-techniques-4" height="68vh">
							<v-alert border="left" colored-border color="yellow lighten-3" elevation="2">
								<v-chip class="mb-2" color="green" x-sm label text-color="white">
									Title
								</v-chip>
								<div v-html='title'></div>
								<v-chip class="mb-2 mt-4" color="green" x-sm label text-color="white">
									Language Tag
								</v-chip>
								<div v-html='language'></div>
							</v-alert>
							<v-alert border="left" colored-border color="yellow lighten-3" elevation="2">
								<div> #Similarity_1
								<br />
								<span class="blue--text">
								 Title : {{sim_title_1.title}}
								 <br />
								 Score : {{sim_title_1.score}}	</span>
								</div>
								<div> #Similarity_2
								<br />
								<span class="blue--text">
								 Title : {{sim_title_2.title}}
								 <br />
								 Score : {{sim_title_2.score}}	</span>
								</div>
								<div> #Similarity_3
								<br />
								<span class="blue--text">
								 Title : {{sim_title_3.title}}
								 <br />
								 Score : {{sim_title_3.score}}	</span>
								</div>
								<div> #Similarity_4
								<br />
								<span class="blue--text">
								 Title : {{sim_title_4.title}}
								 <br />
								 Score : {{sim_title_4.score}}	</span>
								</div>
								<div> #Similarity_5
								<br />
								<span class="blue--text">
								 Title : {{sim_title_5.title}}
								 <br />
								 Score : {{sim_title_5.score}}	</span>
								</div>
							</v-alert>
						</v-sheet>
					</v-card-text>
				</v-card>
			</v-card>
		</v-card>
	</div>
</template>

<script>
	import {
		codemirror
	} from 'vue-codemirror'
	// 核心样式
	import 'codemirror/lib/codemirror.css'
	// 引入主题后还需要在 options 中指定主题才会生效
	import 'codemirror/theme/rubyblue.css'
	import 'codemirror/mode/python/python.js'

	export default {

		data: () => ({
			myData: [],
			page: null,
			loading: false,
			code: '', // 编辑器绑定的值
			options: {
				tabSize: 2, // 缩进格式
				theme: 'base16-light', // 主题，对应主题库 JS 需要提前引入
				lineNumbers: true, // 显示行号
				line: true,
				styleActiveLine: true, // 高亮选中行
				hintOptions: {
					completeSingle: true // 当匹配只有一项的时候是否自动补全
				}
			},
			describe: '',
			title: null,
			language: null,
			sim_title_1: {"title":"","score":''},
			sim_title_2: {"title":"","score":''},
			sim_title_3: {"title":"","score":''},
			sim_title_4: {"title":"","score":''},
			sim_title_5: {"title":"","score":''}
		}),
		components: {
			codemirror
		},
		watch: {
		},
		mounted() {
		},

		methods: {
			requestData: function() {

				this.myData = [];
				this.loading = true
				setTimeout(() => (this.loading = false), 800)

				let postdata = {
					code: this.code,
					describe: this.describe
				}
				
				console.log(postdata)
				
				let net = window.sessionStorage.getItem('net')
				this.postRequest(
					net+"/get_title", postdata
				).then(resp => {
					console.log(resp)
					this.language = resp.language;
					this.title = resp.title;
					this.sim_title_1 = resp.similarity[0]
					this.sim_title_2 = resp.similarity[1]
					this.sim_title_3 = resp.similarity[2]
					this.sim_title_4 = resp.similarity[3]
					this.sim_title_5 = resp.similarity[4]
					this.loading = false
				})
			}
		},

	}
</script>

<style>
</style>
