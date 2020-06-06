import Vue from 'vue'
import App from './App.vue'
import globalMixins from './mixins/globalMixins';
// import $ from 'jquery'
Vue.config.productionTip = false;
Vue.mixin(globalMixins);

new Vue({
  render: h => h(App),
}).$mount('#app');
