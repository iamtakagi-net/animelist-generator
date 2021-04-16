import axios from "axios";
import { Animelist } from "../types/animelist";

export class Client {
  public url: string;

  constructor() {
    this.url = "https://animelist-generator.iamtakagi.net/api/";
  }

  get client() {
    return axios.create({
      baseURL: this.url,
      timeout: 1000 * 60,
    });
  }

  async generate(url: string) {
    const { data } = await this.client.get<Animelist>(`generate?url=${url}`);
    return data;
  }
}
