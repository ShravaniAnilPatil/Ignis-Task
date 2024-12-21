const Header = () => {
    return (
      <header className="bg-white shadow p-4">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold text-blue-600">quickHire.com</h1>
          <div>
            <button className="text-sm font-medium text-blue-600 mx-2">Sign up</button>
            <button className="text-sm font-medium text-blue-600 mx-2">Log in</button>
          </div>
        </div>
      </header>
    );
  };
  
  export default Header;
  