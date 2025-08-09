export class Session {
  private _imageBase64 = "";
  private _loading = false;
  private _name = "";

  get imageBase64(): string {
    return this._imageBase64;
  }

  set imageBase64(value: string) {
    this._imageBase64 = value;
  }

  get loading(): boolean {
    return this._loading;
  }

  set loading(value: boolean) {
    this._loading = value;
  }

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }
}
