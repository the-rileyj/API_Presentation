var v = new Vue({
    el: '#app',
    data: function() {
        return {
            date: "",
            err: "",
            key: "",
            picture: ""
        }
    },
    methods: {
        selectedDate: function(date) {
            this.date = date;
            axios.get(`https://api.nasa.gov/planetary/apod?hd=true&api_key=${this.key}&date=${date}`)
            .then((res) => {
                this.err = "";
                v.picture = res.data.hdurl
            })
            .catch((err) => {
                this.err = err.response.data.msg;
            });
        }
    },
    mounted: function() {
        v = this
        axios.get(window.location.href + "api/creds/nasa")
        .then((res) => {
            v.key = res.data.key
        })
        .catch((err) => {
            //Though not nessesary with how the webserver is structured, this is hypothetically where error handling would go
        });
    }
});