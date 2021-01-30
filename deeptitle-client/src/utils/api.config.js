import axios from 'axios'
import router from '../router'

axios.interceptors.response.use(success => {
	if (success.status && success.status == 200 && success.data.status == 500) {
		console.log(success.data.msg)
		return;
	}
	if (success.data.msg) {
		console.log(success.data.msg)
	}
	return success.data;
}, error => {
	if (error.response.status == 504 || error.response.status == 404) {
		console.log('服务崩溃')
	} else if (error.response.status == 403) {
		console.log('权限不足')
	} else if (error.response.status == 401) {
		console.log('尚未登陆')
		router.replace('/');
	} else {
		if (error.response.data.msg) {
			console.log(error.response.data.msg)
		} else {
			console.log('未知错误!')
		}
	}
	return ;
})

let base = '';



export const postKeyValueRequest = (url, params) => {
	return axios({
		method: 'post',
		url: `${base}${url}`,
		data: params,
		transformRequest: [function(data) {
			let ret = '';
			for (let i in data) {
				ret += encodeURIComponent(i) + '=' + encodeURIComponent(data[i]) + '&'
			}
			return ret;
		}],
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded'
		}
	});
}
export const postRequest = (url, params) => {
	return axios({
		// headers: {
		// 	'Authorization': window.sessionStorage.getItem('Authorization')
		// },
		method: 'post',
		url: `${base}${url}`,
		data: params,
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded'
		}
	})
}
export const putRequest = (url, params) => {
	return axios({
		// headers: {
		// 	'Authorization': window.sessionStorage.getItem('Authorization')
		// },
		method: 'put',
		url: `${base}${url}`,
		data: params
	})
}
export const getRequest = (url, params) => {
	return axios({
		// headers: {
		// 	'Authorization': window.sessionStorage.getItem('Authorization')
		// },
		method: 'get',
		url: `${base}${url}`,
		data: params
	})
}
export const deleteRequest = (url, params) => {
	return axios({
		headers: {
			'Authorization': window.sessionStorage.getItem('Authorization')
		},
		method: 'delete',
		url: `${base}${url}`,
		data: params
	})
}
