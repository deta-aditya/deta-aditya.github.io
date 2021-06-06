export type State<T> = 
| { state: 'INITIAL' }
| { state: 'LOADING' }
| { state: 'SUCCESS', data: T }

export type DataProvider<T> = () => Promise<T>