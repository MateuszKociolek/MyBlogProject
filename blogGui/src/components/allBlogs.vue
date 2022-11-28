<template>
    <div class="allPosts">
        <div v-for="item in blogData" :key="item.id">
            <div class="post">
                    <h2>{{item["title"]}}</h2>
                    <p>{{item["content"]}}</p>
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
                console.log("aba")
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

<style>

:root{
    --postPadding:15px;
}

.allPosts{
    display: flex;
    width: 1fr;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.post{
    width: 600px;
    height: 125px;
    margin-top: 12px;
    margin-bottom: 12px;
    border: 1px black solid;
    padding: var(--postPadding);
    transition: 0.35s;
}

.post > p{
    color: rgb(114, 114, 114);
}
.post:hover{
    padding: calc(var(--postPadding) + 7px);
    font-size: 115%;
}
</style>