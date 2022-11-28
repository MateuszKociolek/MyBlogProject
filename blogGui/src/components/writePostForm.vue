<template>
    <div class="container">
        <a class="goBack" href="index.html">Go to Posts</a>

        <div class="form">
            <label for="title">Title:</label>
            <input v-model="postBody['title']" id="title" name="title" type="text">
            <label for="content">Content:</label>
            <input v-model="postBody['content']" id="content" name="content" type="text">
        </div>

        <button class="sendButton" @click="createPost">Publish Post!</button>
    </div>

</template>

<script>
// import axios from 'axios';
export default {
    data() {
        return {
            postBody: {
                'title': '',
                'content': ''
            }
        }
    },

    methods: {
        createPost() {
            fetch("http://127.0.0.1:8000/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(this.postBody)
            }).then(res => res.json())
                .then(data => console.log(data))
                .catch(err => console.log("Error: ", err))
            this.postBody = {'title': "", 'content': ""}

        }
    },
}
</script>

<style>
    :root{
        --paddingX : 50px;
        --paddingY: 7px;
    }

    .goBack{
        text-decoration: none;
        color: rgb(98, 98, 98);
        background-color: white;
        border: 2px rgba(151, 151, 151, 0.635) solid;
        border-radius: 5px;
        padding: var(--paddingY) var(--paddingX) var(--paddingY) var(--paddingX);
        transition: 0.5s;
        margin-bottom: 10px;
    }

    .goBack:hover{
        /* transition-delay: 0.3s; */

        color: azure;
        background-color: rgba(128, 128, 128, 0.648);
        border-color: rgba(128, 128, 128, 0.648);
        padding: calc(var(--paddingY) + 7px)  calc(var(--paddingX) + 7px) calc(var(--paddingY) + 7px) calc(var(--paddingX) + 7px);
        font-size: 117%;
        
    }


    .sendButton{
        margin-top: 15px;
    }

    .container{
        display: flex;
        flex-direction: column;
        width: 100vw;
        align-items: center;
    }

    .form{
        display: flex;
        flex-direction: column;
    }

    .form > *{
        margin: 5px;
    }
</style>