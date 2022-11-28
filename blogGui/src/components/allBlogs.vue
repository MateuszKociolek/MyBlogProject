<template>
    <div>
        <div v-for="item in blogData" :key="item.id">
            <div class="post">
                <h1>{{item["title"]}}</h1>
                <p>{{item["content"]}}</p>
                {{item}}
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                thisClass:"kutasy",
                blogData: [],
                isActive: true,
            }
        },
        methods: {
            show() {
                this.isActive = !this.isActive
            },
        },
        mounted() {
            fetch("http://127.0.0.1:8000/").
            then(res => res.json())
            .then(data=>this.blogData = data)
            .catch(err=>console.log(err))
        },
    }
</script>

<style scoped>
.post{
    border: 1px black solid;
    width: 25vw;
    padding: 15px;
}

.post:active{
    background-color: red;
}

.active{
    background-color: aqua;
}

.post:focus{
    background-color: red;
}
</style>