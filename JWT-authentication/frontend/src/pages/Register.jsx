import { useState } from 'react'
import axios from 'axios'

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password1: '',
    password2: '',
  })
  const [isLoading, setIsLoading] = useState(false)

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (isLoading) {
      return
    }

    setIsLoading(true)

    try {
      const res = await axios.post(
        'http://127.0.0.1:8000/api/register/',
        formData
      )
      console.log('Success', res.data)
    } catch (error) {
      console.log('Error happened during registration', error.res?.data)
    }
  }

  return (
    <div>
      <h2>Register</h2>
      <form action="" method="post">
        <label htmlFor="">username</label> <br />
        <input
          type="text"
          name="username"
          value={formData.username}
          id=""
          onChange={handleChange}
        />
        <br />
        <br />
        <label htmlFor="">email</label> <br />
        <input
          type="email"
          name="email"
          value={formData.email}
          id=""
          onChange={handleChange}
        />{' '}
        <br />
        <br />
        <label htmlFor="">password</label> <br />
        <input
          type="password"
          name="password1"
          value={formData.password1}
          id=""
          onChange={handleChange}
        />
        <br />
        <br />
        <label htmlFor="">confirm password</label> <br />
        <input
          type="password"
          name="password2"
          value={formData.password2}
          id=""
          onChange={handleChange}
        />
        <br />
        <br />
        <button type="submit" onClick={handleSubmit} disabled={isLoading}>
          Submit
        </button>
      </form>
    </div>
  )
}
export default Register
