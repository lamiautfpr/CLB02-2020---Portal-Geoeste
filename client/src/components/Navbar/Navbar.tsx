import { Link } from 'react-router-dom';
import { logoutUser } from '../../hooks/useAuth';
import {  LogoutButton, Nav, NavItem } from './style';

interface IMenuBurgerProps {
  page?: 'project' | 'resources' | 'home';
  status?: boolean;

}

const NavBar: React.FC<IMenuBurgerProps> = ({ page,  status}) => {

  return (
    <div>
    <Nav>
      <ul>
        <NavItem style={{"marginTop":"3vw"}} active={page === 'resources'} opt={'white'}>
          <Link to ="/categorias/3"
            onClick={()=> window.location.href = '/categorias/3'}
          > 
            MAPAS E DADOS AGROPECUÁRIOS
          </Link>
        </NavItem>
        <NavItem style={{"marginTop":"3vw"}} active={page === 'resources'} opt={'white'}>
          <Link to ="/categorias/1"
            onClick={()=> window.location.href = '/categorias/1'}
          > 
            MAPAS E DADOS AMBIENTAIS
          </Link>
        </NavItem>
        <NavItem active={page === 'home'} opt={'none'}>
          <a href='/'>
              <img style={{"width":"4.4vw", "height":'4.4vw', "marginTop":"-.75vw", "marginLeft":".5vw"}}
                src={require('../../assets/compass_with_p_white.png')}
                onMouseOver={(e)=>{e.currentTarget.src = require('../../assets/compass_with_p_blue.png')}}
                onMouseOut={(e)=>{e.currentTarget.src = require('../../assets/compass_with_p_white.png')}} 
                alt='logo' />
          </a>
        </NavItem>
        <NavItem style={{"marginTop":"3vw"}} active={page === 'project'} opt={'white'}>
          <Link to="/mapas">CONHEÇA O PROJETO</Link>
        </NavItem>
        <NavItem style={{"marginTop":"3.7vw"}} active={page === 'resources'} opt={'white'}>
          <Link to="/publicacoes">PUBLICAÇÕES</Link>
        </NavItem>



      </ul>
    </Nav>
    {status ?(
          <p></p>
        )
        :(
          <LogoutButton>
            <button type="button" onClick={logoutUser}>
              <li> Online </li>
            </button>
          </LogoutButton>
        )
        }
        <br/>
        <br/>
        <br/>
    </div>
  );
};

export default NavBar;


