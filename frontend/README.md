# Frontend Split Expenses Application

This is the frontend application for the Split Expenses project, built using React and TypeScript. The application allows users to manage their expenses, split costs with friends, and keep track of who owes what.

## Getting Started

To get started with the frontend application, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd split-expenses-app/frontend
   ```

2. **Install Dependencies**
   Make sure you have Node.js and npm installed. Then, run:
   ```bash
   npm install
   ```

3. **Run the Application**
   Start the development server:
   ```bash
   npm start
   ```
   The application will be available at `http://localhost:3000`.

## Project Structure

- `src/`: Contains the source code for the application.
  - `App.tsx`: Main application component.
  - `index.tsx`: Entry point for the React application.
  - `components/`: Contains React components.
  - `services/`: Contains API service functions for backend communication.
  - `types/`: Contains TypeScript types and interfaces.

## API Integration

The frontend communicates with the backend REST API to manage expenses. Ensure that the backend server is running and accessible.

## Build for Production

To create a production build of the application, run:
```bash
npm run build
```
This will generate a `build` directory with optimized files for deployment.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.