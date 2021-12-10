//Main
var vueApp = new Vue({
    el: '#portfolioApp',
    delimiters: ['[[', ']]'],
    data:{
        name: "David A. Vargas",
        navMenu: {
            "About":"#aboutMe",
            "Projects":"#projects",
            "Art":"#art",
            "Contact":"#contact",
        },
        showSkills: false,
        showGallery: false,
        showcomics: false,
    },
    methods:{
        saludar: function(){
            alert("Hola")
        },
        skills: function(){
            if (this.showSkills){
                this.showSkills = false;
            }
            else{
                this.showSkills = true;
            }
        },
        gallery: function(){
            if (this.showGallery){
                this.showGallery = false;
            }
            else{
                this.showGallery = true
            }
        },
        comics: function(){
            if (this.showcomics){
                this.showcomics = false;
            }
            else{
                this.showcomics = true;
            }
        },
    }
})