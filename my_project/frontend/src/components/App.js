import React, { Component } from 'react'
import PropTypes from 'prop-types'

const Body = props => {
  const { data } = props
  return (
    <div>
      {data.map((post, i) => {
        return (
          <div key={i}>
            <h2>{post.name}</h2>
            <p>{post.body}</p>
          </div>
        )
      })}
    </div>
  )
}

class App extends Component {
  state = {
    data: [],
    loaded: false,
    placeholder: 'Loading...',
    endpoint: 'http://localhost:3000/api/post',
  }

  componentDidMount() {
    fetch(this.state.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: 'Something went wrong' })
        }

        return response.json()
      })
      .then(data => this.setState({ data: data, loaded: true }))
  }

  render() {
    const { data, loaded, placeholder } = this.state
    return loaded ? <Body data={data} /> : <p>{placeholder}</p>
  }
}

App.propTypes = {}

export default App
