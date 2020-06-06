import $ from 'jquery';

let globalMixins = {
  /**
   * File where all re-usable functions for different functions are put.
   * This is loaded in main js and available in every component through out the app
   * */
  // Load all the sub mixins
  mixins: [],
  data: function () {
    return {
      staticURL: process.env.BASE_URL + process.env.VUE_APP_STATIC_URL,
      words: {
        'error_server': 'Some internal occurred, please try again'
      }
    };
  },
  computed: {},
  methods: {
    ajaxPromise: function (param) {
      /**
       * This is generalized ajax call function, which takes param values and returns promise.
       * It handles error by opening a notification box.
       * @param: {param} A dict containing url, type of request and data as key
       * */
      let contentType = 'application/json;charset=utf-8';
      let mimeType = ''
      if ('contentType' in param) {
        contentType = param.contentType;
      }
      if ('mimeType' in param){
        mimeType = param.mimeType;
      }
      // const self = this;
      console.log("ContentType ", contentType);
      return new Promise(function (resolve, reject) {
        $.ajax({
          url: param.url,
          type: param.type,
          data: param.data,
          processData: false,
          contentType: contentType,
          mimeType: mimeType,
          cache: false,
          success (data) {
            if (data) {
              resolve(data);
            } else {
              resolve(true);
            }
          },
          error (errorData) {
            reject(errorData);
          }
        });
      });
    },
    getBaseURL: function () {
      /** Function to get the base url for API request */
      return window.location.protocol + '//' + window.location.hostname + ':8000';
    }
  },
};

export default globalMixins;