class slider{
    constructor(){
        this.imges=[];
        this.imges[0]="img1"
        this.imges[1]="img2"
        this.imges[2]="img3"
        this.counter=0;
        this.playslider();
        setInterval(()=>{
            this.playslider();
        },3000);

    }
    playslider(){
        if(this.counter<this.imges.length-1){
            this.counter++


        }
        else{
            this.counter=0;

        }
        document.slider_show.src =this.imges[this.counter];
    }
}