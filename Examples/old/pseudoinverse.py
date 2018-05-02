A = np.random.randn(9, 6)
B = np.linalg.pinv(A)
np.allclose(A, np.dot(A, np.dot(B, A)))
np.allclose(B, np.dot(B, np.dot(A, B)))