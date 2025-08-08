export class Response<T> {
  success: boolean;
  message: string;
  data: T | null;

  constructor(data: T | null = null, success = true, message = "") {
    this.data = data;
    this.success = success;
    this.message = message;
  }
}
