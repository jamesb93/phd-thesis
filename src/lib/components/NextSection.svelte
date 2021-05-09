<script>
    export let next;
    export let link;
</script>
<style>
    .btn {
        position: relative;
        /* display: block; */
        margin: 30px auto;
        padding: 5px;
        font-size: 15px;
        overflow: hidden;
        border-width: 0;
        outline: none;
        border-radius: 1px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, .6);    
        background-color: var(--blue);
        color: #ecf0f1;
        transition: background-color .5s;
    }
    
    .btn:hover, .btn:focus {
        background-color: #521b91
    }
    
    .btn > * {
        position: relative;
    }

    .btn > a {
        color: white;
        text-decoration: none;
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
    
    /* Styles, not important */
    *, *:before, *:after {
        box-sizing: border-box;
    }
</style>

<button class="btn orange" type="button">
    <a href={link}>Next Section: {next}</a>
</button>