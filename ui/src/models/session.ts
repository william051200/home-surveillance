export class Session {
  private _name = "";

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }
}
