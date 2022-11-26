<template>
    <div>
        <div v-for="item in blogData" :key="item.id">
            <div class="post">
                <h1>{{item["title"]}}</h1>
                <p>{{item["content"]}}</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                blogData: [],
            }
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
</style>