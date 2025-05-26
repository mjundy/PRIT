document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const orderSection = document.getElementById('order-section');
    const supplierSection = document.getElementById('supplier-section');
    const orderList = document.getElementById('order-list');
    const supplierList = document.getElementById('supplier-list');
    const logoutButton = document.getElementById('logout-button');
    const loginSection = document.getElementById('login-section');

    const apiBaseURL = 'http://localhost:3000';

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = usernameInput.value;
        const password = passwordInput.value;
        
        try {
            const response = await fetch(`${apiBaseURL}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('token', data.token);
                showOrderSection();
                fetchOrders();
                fetchSuppliers();
            } else {
                alert('Login failed');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });

    const showOrderSection = () => {
        loginSection.classList.add('hidden');
        orderSection.classList.remove('hidden');
        supplierSection.classList.remove('hidden');
    };

    const fetchOrders = async () => {
        const token = localStorage.getItem('token');
        if (token) {
            const response = await fetch(`${apiBaseURL}/purchase-orders`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (response.ok) {
                const orders = await response.json();
                orderList.innerHTML = '';
                orders.forEach(order => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${order.item_name} - ${order.status}`;
                    orderList.appendChild(listItem);
                });
            } else {
                alert('Failed to fetch orders');
            }
        }
    };

    const fetchSuppliers = async () => {
        const token = localStorage.getItem('token');
        if (token) {
            const response = await fetch(`${apiBaseURL}/suppliers`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (response.ok) {
                const suppliers = await response.json();
                supplierList.innerHTML = '';
                suppliers.forEach(supplier => {
                    const listItem = document.createElement('li');
                    listItem.textContent = supplier.name;
                    supplierList.appendChild(listItem);
                });
            } else {
                alert('Failed to fetch suppliers');
            }
        }
    };

    logoutButton.addEventListener('click', () => {
        localStorage.removeItem('token');
        loginSection.classList.remove('hidden');
        orderSection.classList.add('hidden');
        supplierSection.classList.add('hidden');
    });

    // Check if user is already logged in
    if (localStorage.getItem('token')) {
        showOrderSection();
        fetchOrders();
        fetchSuppliers();
    }
});
