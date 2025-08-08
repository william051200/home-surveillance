export class Session {
  private _imageBase64 = "";
  private _name = "";

  get imageBase64(): string {
    return this._imageBase64;
  }

  set imageBase64(value: string) {
    this._imageBase64 = value;
  }

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }
}
