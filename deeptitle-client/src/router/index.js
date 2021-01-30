import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Main from '../views/Main/Main.vue'
import Page from '../views/Main/Page.vue'

Vue.use(VueRouter)

const routes = [{
		path: '/',
		name: 'Login',
		component: Login
	}, {
		path: '/home',
		name: 'Home',
		component: Home,
		children: [{
				path: 'main',
				name: 'Main',
				component: Main,
				children: [{
					path: '/main/page',
					name: 'Page',
					component: Page,
				}],
			}
		]
	}
	
]

const router = new VueRouter({
	routes
})

export default router
