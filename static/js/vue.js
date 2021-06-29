//Main
var vueApp = new Vue({
    el: '#portfolioApp',
    delimiters: ['[[', ']]'],
    data:{
        name: "David A. Vargas",
        navMenu: {
            "About Me":"#ilustration",
            "Ilustration":"#ilustration",
            "Web Development":"#ilustration",
            "Comics":"#ilustration",
        },
    }
})