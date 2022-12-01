<template>
    <div class="container">
        <div class="addPost">
            <writePostForm />
        </div>
        <div class="allPosts">
            <div v-for="item in blogData" :key="item.id">
                <div class="post" :class="item['id']">
                    <h2>{{ item["title"] }}</h2>
                    <p>{{ item["content"] }}</p>
                    <button @click="deletePost(item['id'])">Usun</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import writePostForm from './writePostForm.vue'

export default {

    components: {
        writePostForm
    },
    data() {
        return {
            thisClass: "kutasy",
            blogData: [],
            isActive: true,
        }
    },
    methods: {
        show() {
            this.isActive = !this.isActive
            console.log("aba")
        },
        showAllPosts() {
            fetch("http://127.0.0.1:8000/").
                then(res => res.json())
                .then(data => this.blogData = data)
                .catch(err => console.log(err))
        },
        deletePost(id) {
            fetch("http://127.0.0.1:8000/" + id, {
                method: "DELETE",
            }).then(res => res.json())
                .then(data => console.log(data))
                .catch(err => console.log("Error: ", err))
            this.showAllPosts();
            document.location.reload(true);
            this.postBody = { 'title': "", 'content': "" }
        },
    },
    mounted() {
        fetch("http://127.0.0.1:8000/").
            then(res => res.json())
            .then(data => this.blogData = data)
            .catch(err => console.log(err))
    },
}
</script>

<style>
:root {
    --postPadding: 15px;
}

.container{
    display: flex;
    width: auto;
    flex-direction: row;
    justify-content: space-evenly;
}

/* .addPost{
    position: fixed;

} */

.allPosts {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.post {
    width: 600px;
    height: 125px;
    margin-top: 12px;
    margin-bottom: 12px;
    border: 1px black solid;
    padding: var(--postPadding);
    transition: 0.35s;
}

.post>p {
    color: rgb(114, 114, 114);
}

.post:hover {
    padding: calc(var(--postPadding) + 7px);
    font-size: 115%;
}
</style>