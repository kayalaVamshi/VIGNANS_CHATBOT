const express = require("express");
const router = express.Router();
const Content = require("../models/Content");
const verifyToken = require("../middleware/verifyToken"); // We'll add this next

// Create new content
router.post("/", verifyToken, async (req, res) => {
  try {
    const { title, body } = req.body;
    const content = new Content({ title, body, author: req.user.id });
    await content.save();
    res.status(201).json(content);
  } catch (err) {
    res.status(500).json({ error: "Failed to create content" });
  }
});

// Get all content
router.get("/", async (req, res) => {
  try {
    const posts = await Content.find().populate("author", "username");
    res.json(posts);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch content" });
  }
});

module.exports = router;