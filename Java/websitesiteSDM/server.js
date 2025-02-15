// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the app
const app = express();
const port = process.env.PORT || 5000;

// Use body-parser and cors middleware
app.use(bodyParser.json());
app.use(cors());

// Connect to MongoDB
mongoose.connect('YOUR_MONGODB_CONNECTION_STRING', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => console.log('MongoDB connection error:', err));

// Create a schema for applicant data
const applicantSchema = new mongoose.Schema({
    fullName: String,
    email: String,
    phone: String,
    education: String,
    skills: String,
    experience: String,
    jobType: String
});

// Create a model for the applicant data
const Applicant = mongoose.model('Applicant', applicantSchema);

// Route to handle form submissions (POST)
app.post('/submit-application', (req, res) => {
    const newApplicant = new Applicant({
        fullName: req.body.fullName,
        email: req.body.email,
        phone: req.body.phone,
        education: req.body.education,
        skills: req.body.skills,
        experience: req.body.experience,
        jobType: req.body.jobType
    });

    newApplicant.save()
        .then(() => res.status(200).json({ message: 'Application saved successfully!' }))
        .catch(err => res.status(400).json({ message: 'Error saving application', error: err }));
});

// Route to retrieve all applicants (GET)
app.get('/admin/applications', (req, res) => {
    Applicant.find()
        .then(applications => res.json(applications))
        .catch(err => res.status(400).json({ message: 'Error fetching applications', error: err }));
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
