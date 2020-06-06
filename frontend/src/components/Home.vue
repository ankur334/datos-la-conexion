<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12 align-center">
        <h3>Datos</h3>
        <p>Let's try to create connection..</p>
      </div>
      <hr>
      <div class="col-sm-12">
        <label>File
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
        </label>
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-sm-12 align-center">
        <h3>We have following file...</h3>
      </div>
    </div>
    <div
      class="row align-center"
      v-for="(file, index) in files"
      :key="index"
    >
      <div class="col-sm-4">
        <span> {{ file['id'] }}</span>
      </div>
      <div class="col-sm-4">
        <span> {{ file['name'] }}</span>
      </div>
      <div class="col-sm-4">
        <span> {{ file['type'] }}</span>
      </div>
      <br>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    data: function () {
      return {
        files: [],
        file: ''
      };
    },
    mounted () {
      console.log('Called Mounted');
      this.getListOfFile();
    },
    methods: {
      getListOfFile: function () {
        let self = this;
        this.ajaxPromise({
          'url': this.getBaseURL() + '/connections/data-source/',
          'type': 'GET'
        }).then(function (data) {
          console.log('Success ', data);
          self.files = data;
          console.log('This Files ', self.files);
        }).catch(function (error) {
          console.log('Error ', error);
        });
      },
      handleFileUpload () {
        this.file = this.$refs.file.files[0];
        this.uploadFile();
      },
      uploadFile: function () {
        let self = this;
        console.log('This file', this.file);
        let formData = new FormData();
        formData.append('file', this.file);
        formData.append('name', this.file.name);
        formData.append('connection_type', 'FLAT');
        this.ajaxPromise({
          'url': this.getBaseURL() + '/connections/data-source/',
          'mimeType': 'multipart/form-data',
          'contentType': false,
          'data': formData,
          'type': 'POST'
        }).then(function (data) {
          console.log("Data ", data);
          self.getListOfFile();
        }).catch(function (error) {
          console.log('Error ', error);
        });
      }
    }
  };
</script>

<style scoped>

</style>