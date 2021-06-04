<script>
    export let text = "button"
    export let clickHandler = () => {};
    export let selected = null;
</script>

<button 
class:unselected={ selected === false && selected !== null } 
on:click={clickHandler} 
class="btn zoom">
{text}
</button>

<style>
    .btn {
        position: relative;
        min-width: 70px;
        height: 2em;
        font-size: 15px;
        overflow: hidden;
        border-width: 0;
        outline: none;
        border-radius: 1px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, .6);    
        color: #ecf0f1;
        transition: background-color .25s;
        text-align: center;
    }
    
    .btn:before {
        content: "";
        
        position: absolute;
        top: 50%;
        left: 50%;
        
        display: block;
        width: 0;
        padding-top: 0;
        
        border-radius: 100%;
        
        background-color: rgba(236, 240, 241, .3);
        
        -webkit-transform: translate(-50%, -50%);
        -moz-transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        -o-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }
    
    .btn:active:before {
        width: 120%;
        padding-top: 120%;
        transition: width .2s ease-out, padding-top .2s ease-out;
    }
    
    .zoom {
        background-color: var(--blue);
        font-size: 15px;
        min-width: 2em;
    }
    .zoom:hover, .zoom:focus {
        background-color: var(--dark-blue);
    }

    .unselected {
        background-color:grey;
    }

    .unselected:hover, .unselected:focus {
        background-color:rgb(102, 101, 101);
    }
</style>