
var app=new Vue({
  el: '#app',
  data() {
    return{
      message: '',
      log:false,
      goLog:false,
      itemList:[],
      info: null,
      loading: true,
      errored: false,
      tbodylog:0
    }
  },
  methods :{
    
    log1(){
      axios
      
      .get('sql.json', {
        
        params: {
          
            id: this.message,
        },
       timeout: 1000,
      
      })
      .then(response => {
        this.info = response.data
        this.goLog=true
      })
      
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false,this.goLog=false)
    }
    
  }
})

// new Vue({
//   el: '#app',
//   data () {
//     return {
//       info: null,
//       loading: true,
//       errored: false
//     }
//   },
//   filters: {
//     currencydecimal (value) {
//       return value.toFixed(2)
//     }
//   },
//   mounted () {
//     axios
//       .get('https://api.coindesk.com/v1/bpi/currentprice.json')
//       .then(response => {
//         this.info = response.data.bpi
//       })
//       .catch(error => {
//         console.log(error)
//         this.errored = true
//       })
//       .finally(() => this.loading = false)
//   }
// })