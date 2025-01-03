import Signup from './components/signup';
// import Nav from 'react-bootstrap/Nav';
// import Navbar from 'react-bootstrap/Navbar';

// import Container from 'react-bootstrap/Navbar';
function App() {
const user = null;
return (
<div className="App">
<Navbar bg="primary" variant="dark">
<div className="container-fluid">
<Navbar.Brand>TodosApp</Navbar.Brand>
<Nav className="me-auto">
<Container>
<Link class="nav-link" to={"/todos"}>Todos</Link>
{ user ? (
<Link class="nav-link">Logout ({user})</Link>
) : (
<>[DCB3]
<Link class="nav-link" to={"/login"}>Login</Link>
<Link class="nav-link" to={"/signup"}>Sign Up</Link>
</>
)}
</Container>
</Nav>
</div>
</Navbar>
</div>
);
}
export default App;
