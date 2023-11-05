index = 23
input_data = X_test[index].reshape((1, 224, 224, 3))  # Reshape to (1, 224, 224, 3)

predictions = model.predict(input_data)
pred = np.argmax(predictions, axis=1)
print ("Predicted:"+str(pred))
print("original:"+str(y_test[index]))
plt.imshow(X_test[index])  # Display the first image
plt.axis('off')
plt.show()
