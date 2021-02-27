import axios from "axios"

export class Client {
    public url: string

    constructor() {
        this.url = "http://localhost:8000/api/"
    }

    get client() {
        return axios.create({
          baseURL: this.url,
          timeout: 1000*60
        })
    }

    async generate(url: string) {
        const { data } = await this.client.get(`generate?url=${url}`)
        return data
    }
}
