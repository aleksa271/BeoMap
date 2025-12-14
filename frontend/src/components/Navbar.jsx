import React from "react";
import { Navbar, Nav, Container, NavDropdown } from "react-bootstrap";
import BelgradeClock from "./BelgradeClock";

const MyNavbar = () => {
  return (
    <Navbar bg="light" expand="lg" sticky="top">
      <Container>
        <Navbar.Brand href="/">BeoMap</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <div className="ms-auto me-3 fw-semibold text-secondary">
            <BelgradeClock />
          </div>
          <Nav className="ms-auto">
            <Nav.Link href="/">Pocetna</Nav.Link>
            <Nav.Link href="/about">O nama</Nav.Link>
            <Nav.Link href="/favorites">Favoriti</Nav.Link>
            <NavDropdown title="Nalog" id="basic-nav-dropdown">
              <NavDropdown.Item href="/login">Login</NavDropdown.Item>
              <NavDropdown.Item href="/profile">Profil</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default MyNavbar;
